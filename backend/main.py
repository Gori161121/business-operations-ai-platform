from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Business Operations AI Platform API",
    description="Prototype API for business operations, workforce management, reporting and analytics.",
    version="0.1.0"
)

class Employee(BaseModel):
    id: int
    name: str
    role: str
    status: str

class Shift(BaseModel):
    id: int
    employee_id: int
    location: str
    hours: float
    status: str

employees = [
    Employee(id=1, name="Tural Alizada", role="Operations Manager", status="active"),
    Employee(id=2, name="Sample Employee", role="Shift Worker", status="active")
]

shifts = [
    Shift(id=1, employee_id=1, location="Main Location", hours=8.0, status="completed"),
    Shift(id=2, employee_id=2, location="Main Location", hours=6.5, status="completed")
]

@app.get("/")
def root():
    return {
        "project": "Business Operations AI Platform",
        "status": "running",
        "message": "AI-powered business operations prototype API"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees

@app.get("/shifts", response_model=List[Shift])
def get_shifts():
    return shifts

@app.get("/reports/daily")
def daily_report():
    total_hours = sum(shift.hours for shift in shifts)

    return {
        "report_type": "daily_operations_report",
        "total_employees": len(employees),
        "total_shifts": len(shifts),
        "total_worked_hours": total_hours,
        "summary": "Daily operations processed successfully."
    }

@app.get("/analytics/summary")
def analytics_summary():
    total_hours = sum(shift.hours for shift in shifts)

    return {
        "workforce_utilization": "sample_metric",
        "total_worked_hours": total_hours,
        "active_employees": len([e for e in employees if e.status == "active"]),
        "recommendation": "Review shift distribution and monitor workload balance."
    }
