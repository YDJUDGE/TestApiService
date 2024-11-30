from models import Employee, SessionType, Deparment
from .schemas import EmployeeIn
from typing import Union, List
from sqlalchemy.orm import selectinload

def fetch_employee_by_query(q_employee):
    count = q_employee.count()
    employee = q_employee.order_by(Employee.id).all()
    return employee, count

def list_employee(session: SessionType) -> list[Employee]:
    q_employee = session.query(Employee)
    return fetch_employee_by_query(q_employee)

def get_employee_by_department(session: SessionType):
    return ((session.query(Deparment)
            .options(selectinload(Deparment.employee))
            .order_by(Deparment.id.desc()))
            .all()
            )

def create_employee(session: SessionType, employee_in: Union[EmployeeIn, List[EmployeeIn]], dep_id: int) ->list[Employee]:
    if isinstance(employee_in, EmployeeIn):
        employee_in = [employee_in]
    employees = [Employee(**employee.dict(), dep_id=dep_id) for employee in employee_in]
    session.add_all(employees)
    session.commit()

    for employee in employees:
        session.refresh(employee)

    return employees
