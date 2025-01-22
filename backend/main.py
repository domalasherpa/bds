from typing import Union

from fastapi import FastAPI, Body, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from io import BytesIO
from PIL import Image, ImageDraw
import base64
import os

from utils import detect

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/detect-bird/")
async def detect_bird(file: UploadFile = File(...)):
    try:
        # Read the file as bytes
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes))

        # Perform bird detection
        prediction = detect(image)

        draw = ImageDraw.Draw(image)
        for prediction_item in prediction['prediction']:
            box_coords = prediction_item['box_coords']
            label = f"{prediction_item['class']} ({prediction_item['confidence']:.2%})"
            draw.rectangle([tuple(box_coords[:2]), tuple(box_coords[2:])], outline="red", width=3)
            draw.text((box_coords[0], (box_coords[1])-10), label, fill="red")

        # Save the image to a local file
        output_dir = "output_images"
        os.makedirs(output_dir, exist_ok=True)
        image_path = os.path.join(output_dir, file.filename)
        image.save(image_path)

        return {"prediction": prediction['prediction'], "image_path": image_path}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
