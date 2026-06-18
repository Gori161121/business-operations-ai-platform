from backend.services.schedule_matching_service import (
    determine_assignment_method
)


def test_message_match():

    result = determine_assignment_method(
        employee_from_message="Vlad",
        matched_schedule_count=0
    )

    assert result["method"] == "message"


def test_schedule_match():

    result = determine_assignment_method(
        employee_from_message=None,
        matched_schedule_count=1
    )

    assert result["method"] == "schedule"
