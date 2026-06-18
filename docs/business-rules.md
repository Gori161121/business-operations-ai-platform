# Business Rules

## Purpose

This document defines the core operational rules used by the Business Operations AI Platform.

These rules ensure consistency across reporting, revenue calculations, payroll processing, workforce analytics and operational decision support.

---

# Revenue Distribution Rules

## Standard Revenue Split

Revenue generated during a shift is distributed as follows:

| Recipient | Percentage |
|------------|------------|
| Venue | 60% |
| Company | 40% |

Example:

Revenue: 1000 PLN

Venue Share:
600 PLN

Company Share:
400 PLN

---

# Workforce Compensation Rules

## Hourly Compensation

Standard worker compensation:

31.40 PLN / hour

Salary is calculated based on completed worked hours.

Formula:

Salary = Worked Hours × Hourly Rate

---

# Bonus Rules

## Single Worker Shift

If one worker handles the shift:

Bonus = 3% of Company Revenue

Example:

Company Revenue:
1000 PLN

Bonus:
30 PLN

---

## Multiple Workers

If multiple workers are assigned:

Bonus Pool = 3% of Company Revenue

Bonus Pool is divided equally between assigned workers.

Example:

Company Revenue:
1000 PLN

Bonus Pool:
30 PLN

2 Workers:

15 PLN each

---

# Shift Validation Rules

A shift report must contain:

- date
- location
- worker assignment
- worked hours

Missing information triggers manual review.

---

# Assignment Priority Rules

Employee assignment follows the following priority:

## Priority 1

Employee identified directly from report message.

Assignment Method:

message_match

---

## Priority 2

Employee identified through schedule matching.

Assignment Method:

schedule_match

---

## Priority 3

Manual review required.

Reasons:

- no schedule match
- multiple possible matches
- missing information

---

# Review Queue Rules

Reports are sent to manual review when:

- employee cannot be determined
- schedule cannot be matched
- multiple schedule matches exist
- worked hours are missing
- location is unknown

---

# Revenue Tracking Rules

Tracked product categories:

- Free
- Classic
- Premium
- Diamond

Revenue calculations exclude:

- Free products

Revenue calculations include:

- Classic
- Premium
- Diamond

---

# Workforce Analytics Rules

The platform calculates:

- revenue per employee
- revenue per venue
- revenue per shift
- revenue per hour
- workforce utilization
- venue performance

---

# AI Operations Rules

The AI Operations Layer may generate:

- operational summaries
- performance observations
- workload recommendations
- staffing suggestions

AI recommendations are advisory only.

Final decisions remain with management.

---

# Data Integrity Rules

Every report must be traceable.

Required references:

- worker
- venue
- date
- shift

Records without sufficient information are flagged for review.

---

# Future Rules

Potential future additions:

- dynamic bonus calculations
- venue-specific revenue splits
- performance-based incentives
- automated payroll approval
- predictive workforce planning
