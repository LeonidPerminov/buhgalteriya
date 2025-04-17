import pytest
from application.salary import calculate_salary
from application.db.people import get_employees


def test_calculate_salary_output(capfd):
    calculate_salary()
    out, err = capfd.readouterr()
    assert "зарплаты" in out.lower()


def test_get_employees_output(capfd):
    get_employees()
    out, err = capfd.readouterr()
    assert "сотрудник" in out.lower() or "сотрудники" in out.lower()