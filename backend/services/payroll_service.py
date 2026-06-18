"""
Payroll Service

Responsible for:
- Hourly salary calculation
- Bonus calculation
- Total payout calculation
"""

HOURLY_RATE = 31.40
SINGLE_WORKER_BONUS_PERCENTAGE = 0.03


def calculate_salary(worked_hours: float) -> float:
    return round(
        worked_hours * HOURLY_RATE,
        2
    )


def calculate_bonus(
    company_revenue: float,
    worker_count: int
) -> float:

    if worker_count <= 0:
        return 0

    total_bonus = (
        company_revenue
        * SINGLE_WORKER_BONUS_PERCENTAGE
    )

    return round(
        total_bonus / worker_count,
        2
    )


def calculate_total_payout(
    worked_hours: float,
    company_revenue: float,
    worker_count: int
) -> float:

    salary = calculate_salary(
        worked_hours
    )

    bonus = calculate_bonus(
        company_revenue,
        worker_count
    )

    return round(
        salary + bonus,
        2
    )
