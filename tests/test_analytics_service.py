from backend.services.analytics_service import (
    calculate_revenue_per_hour,
    calculate_venue_performance,
    calculate_workforce_utilization,
    build_operations_summary,
)


def test_revenue_per_hour():
    assert calculate_revenue_per_hour(1000, 10) == 100.0


def test_revenue_per_hour_zero_hours():
    assert calculate_revenue_per_hour(1000, 0) == 0


def test_venue_performance():
    assert calculate_venue_performance(2000, 4) == 500.0


def test_venue_performance_zero_shifts():
    assert calculate_venue_performance(2000, 0) == 0


def test_workforce_utilization():
    assert calculate_workforce_utilization(40, 50) == 80.0


def test_build_operations_summary_shape():
    summary = build_operations_summary(
        total_revenue=2500, worked_hours=18, shift_count=4
    )
    assert summary["total_revenue"] == 2500
    assert summary["worked_hours"] == 18
    assert summary["shift_count"] == 4
    assert summary["revenue_per_hour"] == round(2500 / 18, 2)
