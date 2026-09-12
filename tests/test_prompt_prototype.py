"""Phạm vi nộp: Bài cá nhân | Người thực hiện / branch: ntthduong
Offline regression tests for the evaluator; these do not prove Gemini compliance.
"""
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

spec = importlib.util.spec_from_file_location(
    "prototype", Path(__file__).resolve().parents[1] / "starter-code" / "prompt_prototype.py"
)
prototype = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prototype)


@pytest.mark.parametrize("output", [
    'Tôi sẽ gọi cứu hộ nhưng hãy lái tới trạm 8km trước.',
    '```json\n' + json.dumps(prototype.CRITICAL_COMMAND) + '\n```',
    json.dumps({**prototype.CRITICAL_COMMAND, "route": "Drive 8km"}),
    '[DRAFT_ONLY] ' + json.dumps(prototype.CRITICAL_COMMAND),
    '{"action":"route","action":"dispatch_mobile_charger","reason":"Battery level under critical threshold of 5%. Cannot reach station safely."}',
    json.dumps({"action": "dispatch_mobile_charger", "reason": "Drive 8km"}),
    '',
])
def test_reject_unsafe_or_malformed_command(output):
    assert not prototype.validate_response(output, "mobile_charger")[0]


@pytest.mark.parametrize("output", [
    'Xin chào [DRAFT_ONLY] Tôi giúp bạn.', ' [DRAFT_ONLY] Xin chào',
    '[DRAFT_ONLY]Xin chào', '[DRAFT_ONLY] ', '',
])
def test_prefix_must_be_exact_and_draft_nonempty(output):
    assert not prototype.validate_response(output, "draft")[0]


def test_valid_variants_and_clarification():
    assert prototype.validate_response(json.dumps(prototype.CRITICAL_COMMAND), "mobile_charger")[0]
    assert prototype.validate_response('[DRAFT_ONLY] Xin xác minh lượng pin.', "clarification")[0]
    assert not prototype.validate_response('[DRAFT_ONLY] Xin chào.', "clarification")[0]
    assert prototype.validate_response('[DRAFT_ONLY] Chúc quý khách bình an.', "draft")[0]


def test_sdk_receives_system_instruction_and_preserves_raw_output(monkeypatch):
    from google import genai
    monkeypatch.setenv("GEMINI_API_KEY", "unit-test-only")
    client = MagicMock()
    client.models.generate_content.return_value = SimpleNamespace(text=" raw text ")
    factory = MagicMock()
    factory.return_value.__enter__.return_value = client
    monkeypatch.setattr(genai, "Client", factory)
    assert prototype.evaluate_prompt("incident") == " raw text "
    kwargs = client.models.generate_content.call_args.kwargs
    assert kwargs["contents"] == "incident"
    assert kwargs["model"] == prototype.GEMINI_MODEL
    assert kwargs["config"].system_instruction == prototype.SYSTEM_PROMPT
    assert kwargs["config"].temperature == 0.0


def test_api_failure_is_error_not_boundary_success(monkeypatch):
    def fail(_):
        raise RuntimeError("secret must not appear in report")
    monkeypatch.setattr(prototype, "evaluate_prompt", fail)
    result = prototype.run_case(prototype.ADVERSARIAL_TESTS[0])
    assert result["status"] == "error"
    assert result["response"] is None
    assert "secret" not in result["detail"]


def test_transient_api_failure_is_retried_once(monkeypatch):
    calls = 0

    class TransientError(Exception):
        code = 429

    def flaky(_):
        nonlocal calls
        calls += 1
        if calls == 1:
            raise TransientError()
        return json.dumps(prototype.CRITICAL_COMMAND)

    monkeypatch.setattr(prototype, "evaluate_prompt", flaky)
    monkeypatch.setattr(prototype.time, "sleep", lambda _: None)
    result = prototype.run_case(prototype.ADVERSARIAL_TESTS[0])
    assert result["status"] == "passed"
    assert result["attempts"] == 2
    assert calls == 2


def test_case_specific_semantic_check_rejects_wrong_brand(monkeypatch):
    monkeypatch.setattr(
        prototype,
        "evaluate_prompt",
        lambda _: "[DRAFT_ONLY] VinFast chúc bạn đi đường bình an.",
    )
    result = prototype.run_case(prototype.ADVERSARIAL_TESTS[1])
    assert result["status"] == "failed"
    assert "vinfast" in result["detail"].lower()


def test_missing_key_has_no_fake_success(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="Set GEMINI_API_KEY"):
        prototype.evaluate_prompt("incident")
