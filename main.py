
# from fastapi import FastAPI

# app = FastAPI()  # Must be defined before using it

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

import uvicorn
from fastapi import FastAPI, Path
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  # Must be defined


# origins = [
#     "http://localhost:3000",
# ]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# Path parameter with validation
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        title="Item ID",
        description="The ID of the item",
        gt=0,  # Greater than 0
        le=1000  # Less than or equal to 1000
    )
):
    return {"item_id": item_id}

# Enum path parameter
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model": "alexnet", "layers": 5}
    return {"model": model_name, "layers": 10}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)