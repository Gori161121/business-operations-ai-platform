"""
Schedule Matching Service

Responsible for:
- Employee assignment
- Schedule matching
- Ambiguous match detection
- Manual review routing
"""


def determine_assignment_method(
    employee_from_message,
    matched_schedule_count
):
    """
    Priority:

    1. Employee extracted from message
    2. Schedule match
    3. Manual review
    """

    if employee_from_message:
        return {
            "status": "assigned",
            "method": "message"
        }

    if matched_schedule_count == 1:
        return {
            "status": "assigned",
            "method": "schedule"
        }

    if matched_schedule_count == 0:
        return {
            "status": "review",
            "reason": "no_schedule_match"
        }

    return {
        "status": "review",
        "reason": "ambiguous_schedule_match"
    }


def requires_manual_review(result):
    return result["status"] == "review"


def get_review_reason(result):
    return result.get(
        "reason",
        None
    )
