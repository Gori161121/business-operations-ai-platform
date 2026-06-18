"""
AI Summary Service
"""


def generate_operations_summary(
    revenue_per_hour,
    workforce_utilization,
    venue_performance
):

    insights = []

    if revenue_per_hour > 150:
        insights.append(
            "Revenue efficiency is above target."
        )

    if workforce_utilization < 70:
        insights.append(
            "Workforce utilization is below target."
        )

    if venue_performance > 1000:
        insights.append(
            "Venue performance exceeds expected range."
        )

    return {
        "insights": insights
    }
