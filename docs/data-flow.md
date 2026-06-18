# Data Flow

## Purpose

This document describes how operational data moves through the Business Operations AI Platform.

The objective is to transform raw operational reports into structured business intelligence and decision support.

---

# High-Level Flow

```text
Raw Shift Report
        ↓
Data Extraction
        ↓
Validation
        ↓
Schedule Matching
        ↓
Revenue Calculation
        ↓
Payroll Calculation
        ↓
Analytics Processing
        ↓
AI Operations Summary
        ↓
Management Decision
```

---

# Step 1 — Report Submission

Source:

- Worker
- Supervisor
- Operations Manager

Example:

```text
Location: BAILA
Worker: Vlad

Classic: 2
Premium: 1

17:00 - 22:00
```

The platform receives operational information.

---

# Step 2 — Data Extraction

Purpose:

Convert raw operational information into structured records.

Extracted fields:

- location
- worker
- products sold
- worked hours
- shift date

Output:

```json
{
  "location": "BAILA",
  "worker": "Vlad",
  "classic": 2,
  "premium": 1,
  "worked_hours": 5
}
```

---

# Step 3 — Validation

Purpose:

Verify data quality.

Checks:

- worker exists
- location exists
- hours are valid
- report is complete

Possible Results:

```text
VALID
```

or

```text
REQUIRES REVIEW
```

---

# Step 4 — Schedule Matching

Purpose:

Determine worker assignment.

Priority:

1. Message Match
2. Schedule Match
3. Manual Review

Possible Outcomes:

```text
Assigned via Message
Assigned via Schedule
Manual Review Required
```

---

# Step 5 — Revenue Calculation

Purpose:

Calculate operational revenue.

Formula:

Revenue =
Classic Revenue +
Premium Revenue +
Diamond Revenue

Free products are excluded from revenue calculations.

Output:

```text
Total Revenue
Venue Share
Company Share
```

---

# Step 6 — Payroll Calculation

Purpose:

Calculate compensation.

Components:

- salary
- bonus
- total payout

Formula:

```text
Salary =
Worked Hours × Hourly Rate

Bonus =
Company Revenue × Bonus %
```

Output:

```text
Payroll Record
```

---

# Step 7 — Analytics Processing

Purpose:

Generate operational metrics.

Generated Metrics:

- revenue per employee
- revenue per venue
- revenue per shift
- revenue per hour
- workforce utilization
- payroll efficiency

Output:

```text
Analytics Snapshot
```

---

# Step 8 — AI Operations Summary

Purpose:

Convert analytics into management insights.

Example:

```text
Revenue increased by 12%.

Venue BAILA generated the highest
revenue per shift.

Workforce utilization reached 87%.

Recommendation:
Add one additional worker on
Friday evenings.
```

Output:

```text
Operational Insights
```

---

# Step 9 — Management Decision

Purpose:

Support decision-making.

Possible Actions:

- schedule adjustment
- workforce redistribution
- payroll review
- venue optimization
- operational planning

Output:

```text
Management Action
```

---

# Manual Review Flow

```text
Invalid Report
        ↓
Review Queue
        ↓
Manager Review
        ↓
Correction
        ↓
Reprocessing
```

---

# Future Data Sources

Potential future integrations:

- mobile application
- POS systems
- Airtable
- Supabase
- Google Sheets
- WhatsApp Business
- Telegram Bots

---

# End Goal

Transform operational activity into structured, traceable, measurable, and actionable business intelligence.
