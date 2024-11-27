from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import conint

from models import get_session, SessionType
from .schemas import OrderOut, OrderIn, OrderlistOut, ResourceMeta

from . import crud

router = APIRouter(prefix="/orders", tags=["ORDERS"])

@router.get("", response_model=OrderlistOut)
def get_list_orders(skip: int = 0, limit: int = 25, session: SessionType = Depends(get_session)):
    orders_out_objects = []
    orders, count = crud.get_list_orders(session)
    for order in orders:
        order_dict = order.__dict__
        orders_out_objects.append(OrderOut(**order_dict))

    return OrderlistOut(objects=orders_out_objects, meta=ResourceMeta(limit=limit, offset=skip, count=count))

@router.post("", response_model=OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(user_id: int, order_in: OrderIn, session: SessionType = Depends(get_session)):
    return crud.create_order(session, order_in=order_in, user_id=user_id)
