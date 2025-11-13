from fastapi import FastAPI,HTTPException
import uvicorn
import json
from pydantic import BaseModel

class Item(BaseModel):
    price:int

def load_data():
    with open("data.json","r") as f:
        p_data = json.load(f)
    return p_data


def save_data(file,p_data):
    with open(file,"w") as f:
        j_data = json.dumps(p_data,indent=4)
        f.write(j_data)

app = FastAPI()

@app.get("/items/")
def f():
    return load_data()

@app.put("/items/{item_id}")
def update(item_id:int,price:Item):
    data_python = load_data()
    for item in data_python:
        if item["id"] == item_id:
            item["price"] = price.price
            save_data("data.json",data_python)
            return {}
    raise HTTPException(status_code=404,detail="not found")





if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)