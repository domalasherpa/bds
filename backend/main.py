from typing import Union

from fastapi import FastAPI, Body

from io import BytesIO
from PIL import Image
import base64

from utils import detect

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/detect-bird-base64/")
async def detect_bird_base64(image_data: str = Body(...)):
    # Decode base64 image
    image_bytes = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_bytes))

    # Perform bird detection
    prediction = detect(image)
    return prediction