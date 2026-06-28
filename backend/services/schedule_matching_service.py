"""
Schedule Matching Service

Matches raw shift records against scheduled assignments and flags
incomplete or ambiguous shift data for manual review (review queue).
"""

REQUIRED_SHIFT_FIELDS = ("employee_id", "location", "date", "hours")


def detect_missing_shift_data(shift: dict) -> list:
    """Return the required fields that are missing or empty in a raw shift."""
    missing = []
    for field in REQUIRED_SHIFT_FIELDS:
        value = shift.get(field)
        if value is None or value == "":
            missing.append(field)
    return missing


def assign_shift_by_schedule(shift: dict, schedule: list) -> dict:
    """
    Match a raw shift to a scheduled entry (same employee_id + date + location).

    Returns the shift enriched with a status:
      - "matched"      : a matching schedule entry was found
      - "needs_review" : missing data or no schedule match
    """
    missing = detect_missing_shift_data(shift)
    if missing:
        return {**shift, "status": "needs_review", "missing_fields": missing}

    for entry in schedule:
        if (
            entry.get("employee_id") == shift.get("employee_id")
            and entry.get("date") == shift.get("date")
            and entry.get("location") == shift.get("location")
        ):
            return {
                **shift,
                "status": "matched",
                "scheduled_hours": entry.get("hours"),
            }

    return {**shift, "status": "needs_review", "reason": "no_schedule_match"}


def build_review_queue(raw_shifts: list, schedule: list) -> dict:
    """Split raw shifts into matched records and a review queue."""
    matched = []
    review_queue = []

    for shift in raw_shifts:
        result = assign_shift_by_schedule(shift, schedule)
        if result["status"] == "matched":
            matched.append(result)
        else:
            review_queue.append(result)

    return {
        "matched": matched,
        "review_queue": review_queue,
        "matched_count": len(matched),
        "review_count": len(review_queue),
    }


def requires_manual_review(result: dict) -> bool:
    """True if a processed shift needs manual review."""
    return result.get("status") == "needs_review"


def get_review_reason(result: dict):
    """Return why a shift needs review (missing fields or reason), if any."""
    if result.get("missing_fields"):
        return {"missing_fields": result["missing_fields"]}
    return result.get("reason")
