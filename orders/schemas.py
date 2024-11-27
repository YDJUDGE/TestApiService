from pydantic import BaseModel, Field

class BaseOrder(BaseModel):
    adress: str = Field(..., example="ul. Puskhina, d. Kolotuskhina")
    description: str = Field(..., example="This is description")

    class Config:
        from_attributes = True

class OrderIn(BaseOrder):
    pass

class OrderOut(BaseOrder):
    id: int = Field(..., example=123)
    adress: str

    class Config:
        from_attributes = True

class OrderlistOut(BaseModel):
    objects: list[OrderOut]

class ResourceMeta(BaseModel):
    limit: int
    offset: int
    count: int