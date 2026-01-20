from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

# In-memory "database"
items = {}

# -------------------------------
# 1. GET → Retrieve data
# -------------------------------
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}

# -------------------------------
# 2. POST → Create new data
# -------------------------------
@app.post("/items/")
def create_item(item: Item):
    items[item.id] = item
    return {"message": "Item created successfully", "item": item}

# -------------------------------
# 3. PUT → Update/replace data
# -------------------------------
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    items[item_id] = item
    return {"message": "Item updated successfully", "item": item}

# -------------------------------
# 4. PATCH → Partial update
# -------------------------------
@app.patch("/items/{item_id}")
def patch_item(item_id: int, item: dict):
    if item_id not in items:
        return {"error": "Item not found"}
    stored_item = items[item_id].dict()
    stored_item.update(item)
    items[item_id] = Item(**stored_item)
    return {"message": "Item partially updated", "item": items[item_id]}

# -------------------------------
# 5. DELETE → Remove data
# -------------------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}