from pydantic import BaseModel, Field

class BaseEmployee(BaseModel):
    name: str = Field(..., example="Ivan")

    class Config:
        from_attributes = True

class EmployeeIn(BaseEmployee):
    pass

class EmployeeOut(BaseEmployee):
    id: int = Field(..., example=123)
    name: str

    class Config:
        from_attributes = True

class ResourceMeta(BaseModel):
    limit: int
    offset: int
    count: int

class EmployeeListOut(BaseModel):
    objects: list[EmployeeOut]
