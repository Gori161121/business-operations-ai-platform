from backend.services.schedule_matching import (
    detect_missing_shift_data,
    assign_shift_by_schedule,
    build_review_queue,
)


SCHEDULE = [
    {"employee_id": 1, "date": "2026-06-27", "location": "Main", "hours": 8},
]


def test_detect_missing_shift_data_complete():
    shift = {"employee_id": 1, "date": "2026-06-27", "location": "Main", "hours": 8}
    assert detect_missing_shift_data(shift) == []


def test_detect_missing_shift_data_incomplete():
    shift = {"employee_id": 1, "date": "2026-06-27", "location": "Main"}
    assert detect_missing_shift_data(shift) == ["hours"]


def test_assign_shift_matched():
    shift = {"employee_id": 1, "date": "2026-06-27", "location": "Main", "hours": 8}
    result = assign_shift_by_schedule(shift, SCHEDULE)
    assert result["status"] == "matched"
    assert result["scheduled_hours"] == 8


def test_assign_shift_no_match():
    shift = {"employee_id": 9, "date": "2026-06-27", "location": "Other", "hours": 5}
    result = assign_shift_by_schedule(shift, SCHEDULE)
    assert result["status"] == "needs_review"
    assert result["reason"] == "no_schedule_match"


def test_assign_shift_missing_data_goes_to_review():
    shift = {"employee_id": 1, "date": "2026-06-27", "location": "Main"}
    result = assign_shift_by_schedule(shift, SCHEDULE)
    assert result["status"] == "needs_review"
    assert "hours" in result["missing_fields"]


def test_build_review_queue_counts():
    raw = [
        {"employee_id": 1, "date": "2026-06-27", "location": "Main", "hours": 8},
        {"employee_id": 2, "date": "2026-06-27", "location": "Main"},
        {"employee_id": 3, "date": "2026-06-27", "location": "Other", "hours": 5},
    ]
    result = build_review_queue(raw, SCHEDULE)
    assert result["matched_count"] == 1
    assert result["review_count"] == 2
