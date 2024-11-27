from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter(prefix="/users", tags=["USERS"])

from models import get_session, SessionType, User, Order
from .schemas import UserIn, UserOut, UserListOut, ResourceMeta

from . import crud


@router.get("", response_model=UserListOut)
def list_users(username: str = "", skip: int = 0, limit: int = 10,  session: SessionType = Depends(get_session)):
    if username:
        users, count = crud.get_user_by_username_part(session, username)
    else:
        users, count = crud.list_users(session)
    users_out_objects = []
    for user in users[skip: skip + limit]:
        user_dict = user.__dict__
        if user_dict.get('email') is None:
            user_dict['email'] = ""
    users_out_objects.append(UserOut(**user_dict))
    return UserListOut(objects=users_out_objects, meta=ResourceMeta(limit=limit, offset=skip, count=count))

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
