from backend.services.revenue_service import (
    calculate_revenue,
    calculate_company_share,
    calculate_venue_share,
    calculate_average_revenue_per_hour
)


def test_calculate_revenue():
    result = calculate_revenue(
        classic_count=2,
        premium_count=1,
        diamond_count=1,
        classic_price=149,
        premium_price=169,
        diamond_price=249
    )

    assert result == 716


def test_calculate_company_share():
    assert calculate_company_share(1000) == 400


def test_calculate_venue_share():
    assert calculate_venue_share(1000) == 600


def test_calculate_average_revenue_per_hour():
    assert calculate_average_revenue_per_hour(
        total_revenue=800,
        worked_hours=8
    ) == 100
