from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("")
def get_items():
    return[
        {"items": 1},
        {"items": 3}
    ]

@router.post("")
def create_items(data: dict):
    return {"data", data}

@router.get("/{items_id}")
def get_item(item_id: int):
    return{"item_id": item_id}

