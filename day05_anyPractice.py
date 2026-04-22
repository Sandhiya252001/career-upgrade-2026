from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items_db = []


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    items_db.append(item)
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> list[Item]:
    return items_db