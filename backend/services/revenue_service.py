"""
Revenue Calculation Service

Responsible for:
- Revenue calculation
- Venue share calculation
- Company share calculation
- Product revenue aggregation
"""

VENUE_SHARE_PERCENTAGE = 0.60
COMPANY_SHARE_PERCENTAGE = 0.40


def calculate_revenue(
    classic_count: int,
    premium_count: int,
    diamond_count: int,
    classic_price: float,
    premium_price: float,
    diamond_price: float
) -> float:

    return (
        classic_count * classic_price
        + premium_count * premium_price
        + diamond_count * diamond_price
    )


def calculate_company_share(total_revenue: float) -> float:
    return round(
        total_revenue * COMPANY_SHARE_PERCENTAGE,
        2
    )


def calculate_venue_share(total_revenue: float) -> float:
    return round(
        total_revenue * VENUE_SHARE_PERCENTAGE,
        2
    )


def calculate_average_revenue_per_hour(
    total_revenue: float,
    worked_hours: float
) -> float:

    if worked_hours <= 0:
        return 0

    return round(
        total_revenue / worked_hours,
        2
    )
