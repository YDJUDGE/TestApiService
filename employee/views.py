from fastapi import APIRouter, HTTPException, status, Depends
from typing import Union, List

router = APIRouter(prefix="/Employee", tags=["EMPLOYEE"])

from models import get_session, SessionType
from .schemas import EmployeeIn, EmployeeOut, EmployeeListOut, ResourceMeta

from . import crud

@router.get("", response_model=EmployeeListOut)
def list_users(name: str = "", skip: int = 0, limit: int = 10, session: SessionType = Depends(get_session)):
    employee_out_objects = []
    employees, count = crud.list_employee(session)
    for employee in employees:
        employee_dict = employee.__dict__
        employee_out_objects.append(EmployeeOut(**employee_dict))

    return EmployeeListOut(objects=employee_out_objects, meta=ResourceMeta(limit=limit, offset=skip, count=count))

@router.get("/Employee", response_model=EmployeeListOut)
def get_employee_by_dep(session: SessionType = Depends(get_session)):
    q_arr = crud.get_employee_by_department(session)

    emp_out = []
    for dep in q_arr:
        for emp in dep.employee:
            emp_out.append(
                EmployeeOut(
                    id=emp.id,
                    name=emp.name,
                    dep_id=emp.dep_id,
                    created_at=emp.created_at
                )
            )

    return {"objects": emp_out}

@router.post("", response_model=List[EmployeeOut], status_code=status.HTTP_201_CREATED)
def create_employee(dep_id: int, employee_in: Union[EmployeeIn, List[EmployeeIn]], session: SessionType = Depends(get_session)):
    employees = crud.create_employee(session, employee_in=employee_in, dep_id=dep_id)
    return employees
