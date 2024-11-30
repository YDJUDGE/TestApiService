from fastapi import APIRouter, status, Depends

router = APIRouter(prefix="/Department", tags=["DEPARTMENT"])

from models import get_session, SessionType, Deparment
from .schemas import DepartmentIn, DepartmentOut, DepartmentListOut, ResourceMeta
from . import crud

@router.get("", response_model=DepartmentListOut)
def get_list_departments(skip: int = 0, limit: int = 10, session: SessionType = Depends(get_session)):
    department_out_list = []
    departments, count = crud.get_list_departments(session)
    for department in departments:
        department_dict = department.__dict__
        department_out_list.append(DepartmentOut(**department_dict))

    return DepartmentListOut(objects=department_out_list, meta=ResourceMeta(limit=limit, offset=skip, count=count))

@router.get("/Department", response_model=DepartmentListOut)
def get_all_dep_and_emp(session: SessionType = Depends(get_session)):
    q_arr = crud.get_department_by_employee(session)
    dep_out = [
        DepartmentOut(
            id=dep.department.id,
            name_dep=dep.department.name_dep,
            adress_dep=dep.department.adress_dep,
            employees=[{"id": dep.id, "name": dep.name}]
        )
        for dep in q_arr
    ]

    return {"objects": dep_out}

@router.post("", response_model=DepartmentOut, status_code=status.HTTP_201_CREATED)
def create_department(department_in: DepartmentIn, session: SessionType = Depends(get_session)):
    return crud.create_department(session, department_in=department_in)

