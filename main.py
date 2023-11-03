from fastapi import FastAPI
from agent import detect
from firestore import UploadDataToFirestore

app = FastAPI()


# This is route group for
#
# Method : GET
#

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/detect/{image_id}")
async def root(image_id: str):

    # Get data['image', 'count']
    data = await detect(image_id)

    # Upload data to firestore
    r = UploadDataToFirestore(data, image_id)

    return {"message": "success",
            "id": r}


# This is route group for
#
# Method : POST
#
