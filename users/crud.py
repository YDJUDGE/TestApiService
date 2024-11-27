"""
C - create
R - Rename
U - Update
D - Delete
"""

from models import User, SessionType
from .schemas import UserIn
from fastapi import HTTPException, status

def fetch_users_by_query(q_users):
    count = q_users.count()
    users = q_users.order_by(User.id).all()
    return users, count

def list_users(session: SessionType) -> list[User]:
    q_users = session.query(User)
    return fetch_users_by_query(q_users)


def get_user_by_username_part(session: SessionType, username_part: str):
    q_users = session.query(User).filter(User.username.ilike(f"%{username_part}%"))
    return fetch_users_by_query(q_users)

def create_user(session: SessionType, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    session.commit()

    return user

def get_user_by_id(session: SessionType, user_id: int):
    q_user_by_id = session.query(User).filter(User.id == user_id).one_or_none()
    if not q_user_by_id:
        raise HTTPException(status_code=404, detail="User not found")
    return q_user_by_id

def update_user_data(session: SessionType, user_id: int, user_in: UserIn) -> User:
    q_for_upgrade = session.query(User).filter(User.id == user_id).one_or_none()
    if not q_for_upgrade:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_in.dict().items():
        setattr(q_for_upgrade, key, value)
    session.commit()
    return q_for_upgrade

def delete_user_by_id(session: SessionType, user_id: int):
    q_user_for_delete = session.query(User).filter(User.id == user_id).one_or_none()
    if not q_user_for_delete:
        return HTTPException(status_code=404, detail="User not found")
    session.delete(q_user_for_delete)
    session.commit()
    return None
