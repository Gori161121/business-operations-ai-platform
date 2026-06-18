from backend.services.payroll_service import (
    calculate_salary,
    calculate_bonus,
    calculate_total_payout
)


def test_calculate_salary():
    result = calculate_salary(
        worked_hours=10
    )

    assert result == 314.0


def test_calculate_bonus_single_worker():
    result = calculate_bonus(
        company_revenue=1000,
        worker_count=1
    )

    assert result == 30.0


def test_calculate_bonus_two_workers():
    result = calculate_bonus(
        company_revenue=1000,
        worker_count=2
    )

    assert result == 15.0


def test_calculate_total_payout():
    result = calculate_total_payout(
        worked_hours=10,
        company_revenue=1000,
        worker_count=1
    )

    assert result == 344.0
