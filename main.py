# Import Union since our Item object will have tags that can be strings or a list.
from typing import Union, Optional

from fastapi import FastAPI
# BaseModel from Pydantic is used to define data objects.
from pydantic import BaseModel

# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int

app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}

# This allows sending of data (our TaggedItem) via POST to the API.
@app.post("/items/")
async def create_item(item: TaggedItem):
    return item

# A GET that in this case just returns the item_id we pass,
# but a future iteration may link the item_id here to the one we defined in our TaggedItem.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}


class Body(BaseModel):
    name: str

@app.post("/exercise_function/{path}")
async def exercise_function(path: int, query: int, body: Body):
  return {"path": path, "query": query, "body": body}