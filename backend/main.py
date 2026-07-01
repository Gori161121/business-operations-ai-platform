from contextlib import asynccontextmanager
from typing import List

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlmodel import Session, select

from backend.database import get_session, init_db
from backend.models import Employee, Shift
from backend.services.revenue_service import (
    calculate_revenue,
    calculate_company_share,
    calculate_venue_share,
)
from backend.services.payroll_service import (
    calculate_salary,
    calculate_bonus,
    calculate_total_payout,
)
from backend.services.analytics_service import (
    build_operations_summary,
)
from backend.services.ai_summary_service import (
    generate_operations_summary,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables and seed initial data on startup.
    init_db()
    from backend.seed import seed
    seed()
    yield


app = FastAPI(
    title="Business Operations AI Platform API",
    description="Prototype API for business operations, workforce management, reporting and analytics.",
    version="0.2.0",
    lifespan=lifespan,
)


class EmployeeCreate(BaseModel):
    full_name: str
    role: str
    phone: str | None = None
    email: str | None = None
    status: str = "active"


class OperationsInput(BaseModel):
    total_revenue: float
    worked_hours: float
    shift_count: int


@app.get("/")
def root():
    return {
        "project": "Business Operations AI Platform",
        "status": "running",
        "message": "AI-powered business operations prototype API",
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/employees", response_model=List[Employee])
def get_employees(session: Session = Depends(get_session)):
    return session.exec(select(Employee)).all()


@app.post("/employees", response_model=Employee, status_code=201)
def create_employee(payload: EmployeeCreate, session: Session = Depends(get_session)):
    employee = Employee(**payload.model_dump())
    session.add(employee)
    session.commit()
    session.refresh(employee)
    return employee


@app.get("/shifts", response_model=List[Shift])
def get_shifts(session: Session = Depends(get_session)):
    return session.exec(select(Shift)).all()


@app.get("/reports/daily")
def daily_report(session: Session = Depends(get_session)):
    shifts = session.exec(select(Shift)).all()
    employees = session.exec(select(Employee)).all()
    total_hours = sum(shift.worked_hours for shift in shifts)
    return {
        "report_type": "daily_operations_report",
        "total_employees": len(employees),
        "total_shifts": len(shifts),
        "total_worked_hours": total_hours,
        "summary": "Daily operations processed successfully.",
    }


@app.get("/analytics/summary")
def analytics_summary(session: Session = Depends(get_session)):
    shifts = session.exec(select(Shift)).all()
    employees = session.exec(select(Employee)).all()
    total_hours = sum(shift.worked_hours for shift in shifts)
    return {
        "workforce_utilization": "sample_metric",
        "total_worked_hours": total_hours,
        "active_employees": len([e for e in employees if e.status == "active"]),
        "recommendation": "Review shift distribution and monitor workload balance.",
    }


@app.get("/revenue/example")
def revenue_example():
    total_revenue = calculate_revenue(
        classic_count=2,
        premium_count=1,
        diamond_count=1,
        classic_price=149,
        premium_price=169,
        diamond_price=249,
    )
    return {
        "total_revenue": total_revenue,
        "venue_share": calculate_venue_share(total_revenue),
        "company_share": calculate_company_share(total_revenue),
    }


@app.get("/payroll/example")
def payroll_example():
    return {
        "salary": calculate_salary(10),
        "bonus": calculate_bonus(company_revenue=1000, worker_count=1),
        "total_payout": calculate_total_payout(
            worked_hours=10,
            company_revenue=1000,
            worker_count=1,
        ),
    }


@app.get("/analytics/operations")
def operations_analytics():
    return build_operations_summary(
        total_revenue=2500,
        worked_hours=18,
        shift_count=4,
    )


@app.post("/ai/summarize")
def ai_summarize(data: OperationsInput):
    return generate_operations_summary(data.model_dump())
