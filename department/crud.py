from models import Deparment, SessionType, Employee
from .schemas import DepartmentIn, DepartmentOut
from sqlalchemy.orm import selectinload

def fetch_departments_by_query(q_department) -> tuple[list[Deparment], int]:
    count = q_department.count()
    departments = q_department.order_by(Deparment.id).all()
    return departments, count

def get_list_departments(session: SessionType):
    q_departments = session.query(Deparment)
    return fetch_departments_by_query(q_departments)

def get_department_by_employee(session: SessionType):
    return (session.query(Employee)
            .options(selectinload(Employee.department))
            .order_by(Employee.dep_id).all()
            )

def create_department(session: SessionType, department_in: DepartmentIn) -> Deparment:
    department = Deparment(**department_in.dict())
    session.add(department)
    session.commit()

    return DepartmentOut.from_orm(department)



