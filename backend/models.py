"""
ORM models (SQLModel) aligned with database/schema.sql.
"""

from datetime import date, datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Employee(SQLModel, table=True):
    __tablename__ = "employees"

    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    role: str
    phone: Optional[str] = None
    email: Optional[str] = None
    status: str = "active"
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Location(SQLModel, table=True):
    __tablename__ = "locations"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    city: Optional[str] = None
    address: Optional[str] = None
    status: str = "active"


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: Optional[int] = Field(default=None, primary_key=True)
    product_name: str
    category: Optional[str] = None
    price: float
    is_active: bool = True


class Shift(SQLModel, table=True):
    __tablename__ = "shifts"

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employees.id")
    location_id: Optional[int] = Field(default=None, foreign_key="locations.id")
    shift_date: date
    worked_hours: float = 0.0
    status: str = "scheduled"


class SalesReport(SQLModel, table=True):
    __tablename__ = "sales_reports"

    id: Optional[int] = Field(default=None, primary_key=True)
    shift_id: Optional[int] = Field(default=None, foreign_key="shifts.id")
    free_count: int = 0
    classic_count: int = 0
    premium_count: int = 0
    diamond_count: int = 0
    revenue: float = 0.0
