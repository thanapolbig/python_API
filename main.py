from typing import Optional
import sqlite3
from fastapi import FastAPI

app = FastAPI()

print("go to swagger =>> http://127.0.0.1:8000/docs")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/getdata")

