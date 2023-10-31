from fastapi import FastAPI
from agent import get_img

app = FastAPI()


# This is route group for
#
# Method : GET
#

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_img")
async def root():
    img = await get_img()
    return {"message": img}


# This is route group for
#
# Method : POST
#
