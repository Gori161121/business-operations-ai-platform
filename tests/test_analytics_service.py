from backend.services.analytics_service import (
    calculate_revenue_per_hour
)


def test_revenue_per_hour():

    result = calculate_revenue_per_hour(
        revenue=1000,
        worked_hours=10
    )

    assert result == 100
