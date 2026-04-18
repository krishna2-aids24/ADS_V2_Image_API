import os
import numpy as np
from tensorflow.keras.models import load_model

from ADS_V2_Layers.ADS_V2_Image_Layers.ADS_V2_Image_Preprocessing import preprocess_image
from ADS_V2_Layers.ADS_V2_Image_Layers.ADS_V2_Image_Treatment_Layer import get_image_treatment

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "ADS_V2_Models",
    "ADS_V2_Image_Model",
    "dog_disease_model.h5"
)
model = load_model(MODEL_PATH)


# Class labels must match training order
CLASS_LABELS = [
    "Dermatitis",
    "Fungal infections",
    "Healthy",
    "Hypersensitivity",
    "Demodicosis",
    "Ringworm"
]


def predict_disease(image_path):

    # preprocess image
    processed_image = preprocess_image(image_path)

    # prediction
    predictions = model.predict(processed_image)

    class_index = np.argmax(predictions)

    confidence = float(np.max(predictions))

    predicted_disease = CLASS_LABELS[class_index]

    # get treatment
    treatment = get_image_treatment(predicted_disease)

    result = {
        "prediction": {
            "disease": predicted_disease,
            "confidence": round(confidence * 100, 2)
        },
        "treatment": treatment
    }

    return result