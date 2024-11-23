from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str = Field(..., example="Ivan Ivanov")
    email: str = Field(..., example="Exam@ple.com")

    class Config:
        from_attributes = True

class UserIn(UserBase):
    pass

class UserOut(UserBase):
    id: int = Field(..., example=123)

    class Config:
        from_attributes = True

class UserListOut(BaseModel):
    objects: list[UserOut]
