from fastapi import FastAPI, Response
import cv2
import numpy as np
import torch
from fastapi.responses import StreamingResponse
from utils import detect

# Initialize FastAPI app
app = FastAPI()

# Load a pre-trained YOLOv5 model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Use YOLOv5 small model

# OpenCV Video Capture
cap = cv2.VideoCapture(0)  # Use your camera or RTSP stream here (e.g., 'rtsp://<url>')

def generate_frames():
    while True:
        # Capture frame from video stream
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform object detection on the frame
        annotated_frame = detect(frame)  # Perform inference with YOLOv5
        
        # Annotate the frame with results (bounding boxes, labels, etc.)
        # annotated_frame = results.render()[0]  # Render the results onto the frame
        
        # Encode the frame into JPEG format
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        if not ret:
            continue
        
        # Convert to byte array for streaming
        frame_bytes = buffer.tobytes()
        
        # Yield the frame as a byte stream for real-time video
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

@app.get("/video_feed")
def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

# @app.post("/detect-bird-base64/")
# async def detect_bird_base64(image_data: str = Body(...)):  # Expecting a string (base64)
#     try:
#         # Debug: Print the first 50 characters of the received base64 image
#         print(f"Received image data (first 50 chars): {image_data[:50]}...")

#         # Decode base64 image
#         image_bytes = base64.b64decode(image_data)
#         image = Image.open(BytesIO(image_bytes))

#         # Perform bird detection
#         prediction = detect(image)

#         # Return prediction as a JSON response
#         return {"prediction": prediction}

#     except Exception as e:
#         print(f"Error: {e}")
#         return {"error": str(e)}  #
