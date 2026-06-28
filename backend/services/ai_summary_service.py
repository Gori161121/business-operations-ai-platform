"""
AI Operations Summary Service

Generates a short operations summary with recommendations.
Uses OpenAI (gpt-4o-mini) when OPENAI_API_KEY is set, otherwise a
rule-based fallback so the endpoint works without an API key.
"""

import os
import json


def _rule_based_summary(data: dict) -> dict:
    revenue = float(data.get("total_revenue", 0) or 0)
    worked_hours = float(data.get("worked_hours", 0) or 0)
    shift_count = int(data.get("shift_count", 0) or 0)

    revenue_per_hour = round(revenue / worked_hours, 2) if worked_hours else 0.0

    recommendations = []
    if revenue_per_hour and revenue_per_hour < 50:
        recommendations.append(
            "Revenue per worked hour is low — review staffing against demand."
        )
    else:
        recommendations.append("Revenue per worked hour looks healthy.")

    if shift_count and (worked_hours / shift_count) < 4:
        recommendations.append(
            "Average shift length is short — consider consolidating shifts."
        )

    if revenue > 5000:
        recommendations.append("Revenue above 5000 — bonus threshold reached.")

    return {
        "summary": (
            f"Revenue {revenue:.0f} across {shift_count} shifts and "
            f"{worked_hours:.0f} worked hours ({revenue_per_hour:.2f} per hour)."
        ),
        "recommendations": recommendations,
        "generated_with": "rule-based-fallback",
    }


def _openai_summary(data: dict) -> dict:
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    prompt = (
        "You are an operations analyst. Given this JSON of daily operations "
        "metrics, return JSON with keys 'summary' (2-3 sentences) and "
        "'recommendations' (an array of 3 short action strings).\n\n"
        f"{json.dumps(data)}"
    )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.4,
    )

    result = json.loads(response.choices[0].message.content)
    result["generated_with"] = "openai"
    return result


def generate_operations_summary(data: dict) -> dict:
    """Return an operations summary. Uses OpenAI if configured, else fallback."""
    if os.getenv("OPENAI_API_KEY"):
        try:
            return _openai_summary(data)
        except Exception:
            return _rule_based_summary(data)
    return _rule_based_summary(data)
