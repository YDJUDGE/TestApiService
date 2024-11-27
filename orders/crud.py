from models import Order, SessionType
from .schemas import OrderIn


def fetch_orders_by_query(q_order):
    count = q_order.count()
    orders = q_order.order_by(Order.id).all()
    return orders, count

def get_list_orders(session: SessionType) -> list[Order]:
    q_order = session.query(Order)
    return fetch_orders_by_query(q_order)

def create_order(session: SessionType, order_in: OrderIn, user_id: int) -> Order:
    order = Order(**order_in.dict(), user_id=user_id)
    session.add(order)
    session.commit()

    return order