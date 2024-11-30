from pydantic import BaseModel, Field

class BaseDepartment(BaseModel):
    name_dep: str = Field(..., example="Marketing")
    adress_dep: str = Field(..., example="Los Angeles")

    class Config:
        from_attributes = True

class DepartmentIn(BaseDepartment):
    pass

class DepartmentOut(BaseDepartment):
    id: int = Field(..., example=123)
    # name_dep: str
    # adress_dep: str

    class Config:
        from_attributes = True

class ResourceMeta(BaseModel):
    limit: int
    offset: int
    count: int

class DepartmentListOut(BaseModel):
    objects: list[DepartmentOut]



