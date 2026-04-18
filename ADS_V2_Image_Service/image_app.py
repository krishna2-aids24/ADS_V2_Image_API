from fastapi import FastAPI, UploadFile, File
import shutil
import os

# 🔥 import your image prediction function
from ADS_V2_Layers.ADS_V2_Image_Layers.ADS_V2_Image_Prediction_Layer import predict_disease

app = FastAPI()

UPLOAD_FOLDER = "temp_images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/predict-image")
async def predict_image(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded image
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔥 Run your TensorFlow model
    result = predict_disease(file_path)

    return result