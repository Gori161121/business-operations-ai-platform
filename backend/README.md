# Backend

FastAPI prototype backend for the Business Operations AI Platform.

---

## Current Features

- Employee API
- Shift API
- Daily Reporting API
- Analytics Summary API
- Revenue Calculation API
- Payroll Calculation API
- Operations Analytics API
- Health Check Endpoint

---

## Domain Services

| Service | Purpose |
|---|---|
| `revenue_service.py` | Revenue, venue share and company share calculations |
| `payroll_service.py` | Salary, bonus and payout calculations |
| `analytics_service.py` | Revenue per hour, venue performance and workforce metrics |
| `schedule_matching_service.py` | Assignment method, schedule matching and manual review routing |
| `ai_summary_service.py` | Basic AI-style operations summary logic |

---

## Available Endpoints

```text
GET /
GET /health
GET /employees
GET /shifts
GET /reports/daily
GET /analytics/summary
GET /revenue/example
GET /payroll/example
GET /analytics/operations
```

---

## Testing

Unit tests are located in:

```text
tests/
```

Run tests:

```bash
pytest
```

---

## Development Commands

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run API:

```bash
uvicorn backend.main:app --reload
```

---

## CI

This repository includes a GitHub Actions workflow for backend tests.

```text
.github/workflows/ci.yml
```

---

## Planned Features

- Authentication
- Role Management
- Workforce Scheduling
- Reporting Engine
- Workflow Automation
- AI Operations Assistant
- Business Intelligence Layer
