import os
import tempfile

# Use an isolated temp SQLite database for this test module.
_TEST_DB = os.path.join(tempfile.gettempdir(), "boaip_db_test.db")
if os.path.exists(_TEST_DB):
    os.remove(_TEST_DB)
os.environ["DATABASE_URL"] = f"sqlite:///{_TEST_DB}"

from sqlmodel import Session, select  # noqa: E402

from backend.database import engine, init_db  # noqa: E402
from backend.models import Employee, Shift  # noqa: E402
from backend.seed import seed  # noqa: E402


def test_init_and_seed():
    init_db()
    seed()
    with Session(engine) as session:
        employees = session.exec(select(Employee)).all()
        shifts = session.exec(select(Shift)).all()
    assert len(employees) >= 2
    assert any(e.full_name == "Tural Alizada" for e in employees)
    assert len(shifts) >= 2


def test_seed_is_idempotent():
    seed()
    seed()
    with Session(engine) as session:
        employees = session.exec(select(Employee)).all()
    # No duplicates created by repeated seeding.
    assert len([e for e in employees if e.full_name == "Tural Alizada"]) == 1
