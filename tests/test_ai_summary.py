import os

from backend.services.ai_summary import generate_operations_summary


def _no_api_key():
    # Force the deterministic fallback path for these tests.
    os.environ.pop("OPENAI_API_KEY", None)


def test_summary_uses_fallback_without_key():
    _no_api_key()
    result = generate_operations_summary(
        {"total_revenue": 2500, "worked_hours": 18, "shift_count": 4}
    )
    assert result["generated_with"] == "rule-based-fallback"
    assert result["summary"]
    assert isinstance(result["recommendations"], list)
    assert len(result["recommendations"]) >= 1


def test_summary_flags_bonus_threshold():
    _no_api_key()
    result = generate_operations_summary(
        {"total_revenue": 6000, "worked_hours": 40, "shift_count": 8}
    )
    joined = " ".join(result["recommendations"]).lower()
    assert "bonus threshold" in joined


def test_summary_handles_zero_hours():
    _no_api_key()
    result = generate_operations_summary(
        {"total_revenue": 0, "worked_hours": 0, "shift_count": 0}
    )
    assert result["generated_with"] == "rule-based-fallback"
    assert "summary" in result
