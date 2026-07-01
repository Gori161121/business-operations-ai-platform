"""
Seed initial data so the API returns meaningful results on first run.
Safe to call repeatedly — it only seeds when the tables are empty.
"""

from datetime import date

from sqlmodel import Session, select

from backend.database import engine
from backend.models import Employee, Location, Shift


def seed() -> None:
    with Session(engine) as session:
        if session.exec(select(Employee)).first():
            return

        location = Location(name="Main Location", city="Warsaw")
        session.add(location)

        employees = [
            Employee(full_name="Tural Alizada", role="Operations Manager"),
            Employee(full_name="Sample Employee", role="Shift Worker"),
        ]
        for employee in employees:
            session.add(employee)

        session.commit()
        session.refresh(location)
        for employee in employees:
            session.refresh(employee)

        session.add(
            Shift(
                employee_id=employees[0].id,
                location_id=location.id,
                shift_date=date.today(),
                worked_hours=8.0,
                status="completed",
            )
        )
        session.add(
            Shift(
                employee_id=employees[1].id,
                location_id=location.id,
                shift_date=date.today(),
                worked_hours=6.5,
                status="completed",
            )
        )
        session.commit()
