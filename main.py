from fastapi import FastAPI

from pydantic import constr

from users.views import router as users_router
from items_views import router as items_router
# from orders.views import router as router_orders


app = FastAPI()
app.include_router(users_router)
app.include_router(items_router)
# app.include_router(router_orders)

@app.get("/")
def root():
    return {"message": "This is the test!"}

@app.get("/hello")
def hello(name: constr(min_length=3) = "Unknown"):
    return {"message": f"Hello, {name}", "name": name}


@app.get("/add")
def add(a: int, b: int):
    return{
        "a": a,
        "b": b,
        "sum": a + b
    }

