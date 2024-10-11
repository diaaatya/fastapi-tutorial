from enum import Enum
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class Category(Enum):
    FOOD = "food"
    DRINKS = "drinks"
    SNACKS = "snacks"


class item(BaseModel):
    name: str
    price: float
    category: Category
    id: int
    count: int 


items = {
    1: item(name="apple", price=10, count=10, id=1, category=Category.FOOD),
    2: item(name="Cola", price=20, count=10, id=2, category=Category.DRINKS),
    3: item(name="Cheese", price=30, count=10, id=3, category=Category.FOOD),
    4: item(name="chips", price=40, count=10, id=4, category=Category.SNACKS),
}

@app.get("/")
def index():
    return {"items" : items}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item {item_id=}not found")
    return items[item_id]

@app.get("/items")
def query_item_by_parameters(
    name: Optional[str] = None,
    price: Optional[float] = None,
    count: Optional[int] = None,
    category: Optional[Category] = None
):
        selection = [
        item.dict() for item in items.values()
        if (name is None or item.name == name)
        and (price is None or item.price == price)
        and (count is None or item.count == count)
        and (category is None or item.category == category)
    ]
        return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }

@app.post("/")
def create_item(item: item):
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item {item.id} already exists")
    items[item.id] = item
    return items

@app.delete("/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    item = items.pop(item_id)
    return items

@app.put("/items/{item_id}")
def update(
    item_id: int,
    name: Optional[str] = None,
    price: Optional[float] = None,
    count: Optional[int] = None,
    category: Optional[Category] = None
):
    if item_id not in items:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    if all (info is None for info in (name, price, count, category)):
        raise HTTPException(status_code=400, detail="No data to update")    
    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count
    if category is not None:
        item.category = category
    return {"updated items": items}
