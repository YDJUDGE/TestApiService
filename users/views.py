from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter(prefix="/users", tags=["USERS"])

from models import get_session, SessionType, User
from .schemas import UserIn, UserOut, UserListOut

from . import crud


@router.get("", response_model=UserListOut)
def list_users(username: str = "", session: SessionType = Depends(get_session)):
    if username:
        users, count = crud.get_user_by_username_part(session, username)
    else:
        users, count = crud.list_users(session)
    users_out_objects =[UserOut.from_orm(user) for user in users]
    return UserListOut(objects=users_out_objects)

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserIn, session: SessionType = Depends(get_session)):
    return crud.create_user(session, user_in=user_in)

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, session: SessionType = Depends(get_session)):
    return crud.get_user_by_id(session, user_id=user_id)

@router.put("/{user_id}")
def upgrade_user_data(user_id: int, user_in: UserIn, session: SessionType = Depends(get_session)):
    return crud.update_user_data(session, user_id=user_id, user_in=user_in)

@router.delete("/{user_id}")
def delete_user(user_id: int, session: SessionType = Depends(get_session)):
    return crud.delete_user_by_id(session, user_id=user_id)
