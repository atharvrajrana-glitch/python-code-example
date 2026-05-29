from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Sample database
items_db = []


# Pydantic model
class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


# Home route
@app.get("/")
async def home():
    return {"message": "FastAPI is running 🚀"}


# Health check
@app.get("/health")
async def health():
    return {"status": "OK"}


# Get all items
@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db


# Get single item
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")


# Create item
@app.post("/items")
async def create_item(item: Item):
    items_db.append(item)
    return {
        "message": "Item created successfully",
        "item": item
    }


# Delete item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            deleted = items_db.pop(index)
            return {
                "message": "Item deleted",
                "item": deleted
            }

    raise HTTPException(status_code=404, detail="Item not")