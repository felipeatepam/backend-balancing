"""Example of fastapi main file."""
from typing import Union
import os
from fastapi import FastAPI

app = FastAPI()
host = os.getenv("HOSTNAME", "fail")

@app.get("/")
def read_root():
    """Returns Hello World."""
    return {"Hello": "World"}

@app.get("/api/hello")
def hello():
    """Returns Hello World."""
    return f'Response received from pod: {host}'

@app.get("/items/{item_id}")
def read_item(item_id: int, item_count: Union[str, None] = None):
    """Returns numbers of items."""
    return {"item_id": item_id, "q": item_count}
