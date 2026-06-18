"""
Analytics Service

Responsible for:
- Revenue analytics
- Workforce analytics
- Venue performance analytics
- Productivity metrics
"""


def calculate_revenue_per_hour(
    revenue: float,
    worked_hours: float
) -> float:

    if worked_hours <= 0:
        return 0

    return round(
        revenue / worked_hours,
        2
    )


def calculate_employee_productivity(
    revenue: float,
    worked_hours: float
) -> float:

    if worked_hours <= 0:
        return 0

    return round(
        revenue / worked_hours,
        2
    )


def calculate_venue_performance(
    total_revenue: float,
    shift_count: int
) -> float:

    if shift_count <= 0:
        return 0

    return round(
        total_revenue / shift_count,
        2
    )


def calculate_workforce_utilization(
    worked_hours: float,
    available_hours: float
) -> float:

    if available_hours <= 0:
        return 0

    return round(
        (worked_hours / available_hours) * 100,
        2
    )


def build_operations_summary(
    total_revenue: float,
    worked_hours: float,
    shift_count: int
):

    return {
        "revenue_per_hour":
            calculate_revenue_per_hour(
                total_revenue,
                worked_hours
            ),

        "venue_performance":
            calculate_venue_performance(
                total_revenue,
                shift_count
            ),

        "total_revenue":
            total_revenue,

        "worked_hours":
            worked_hours,

        "shift_count":
            shift_count
    }
