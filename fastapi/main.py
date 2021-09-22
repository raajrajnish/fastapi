from fastapi import FastAPI
from typing import Union, Optional
from pydantic import BaseModel

# initiate the app
app = FastAPI()


# simple fast api
@app.get("/helloWorld")
async def Greeting():
    return "Hello world!"


# declare the pydantic data model
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int


# using pydantic data model
@app.post("/items/")
async def create_item(item: TaggedItem):
    return item


# path and query parameters
# parameters not declared in the path are automatically query parameters.

@app.get("/items/{item_id}/")
async def get_items(item_id: int, count: int = 1):
    return "fetched {} items for item id {}".format(count, item_id)


# to create optional query parameters use Optional from the typing module.
@app.get("/items/{item_id}/")
async def get_items(item_id: int, count: int = 1, temp: Optional[str] = None):
    return "fetched {} items for item id {}".format(count, item_id)

# how to run fast api - go to root directory main.py where app is defined and run below command
# uvicorn main:app --reload
