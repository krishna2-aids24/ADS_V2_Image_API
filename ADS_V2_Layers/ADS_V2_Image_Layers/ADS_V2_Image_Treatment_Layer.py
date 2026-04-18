# ==========================================
# IMAGE DISEASE TREATMENT DATABASE
# ==========================================

IMAGE_TREATMENT_DB = {

    "Dermatitis": {
        "medication": [
            "Topical corticosteroids",
            "Antihistamines",
            "Medicated shampoos"
        ],
        "supportive_care": [
            "Maintain skin hygiene",
            "Avoid allergens",
            "Regular veterinary monitoring"
        ],
        "notes": "Skin inflammation caused by infection, allergy, or irritation."
    },

    "Fungal infections": {
        "medication": [
            "Topical antifungal creams",
            "Itraconazole or Ketoconazole"
        ],
        "supportive_care": [
            "Keep affected area dry",
            "Maintain hygiene",
            "Isolate infected animal if contagious"
        ],
        "notes": "Common fungal skin infections require antifungal therapy."
    },

    "Healthy": {
        "medication": [],
        "supportive_care": [
            "Maintain balanced diet",
            "Regular grooming",
            "Routine veterinary checkups"
        ],
        "notes": "No disease detected."
    },

    "Hypersensitivity": {
        "medication": [
            "Antihistamines",
            "Corticosteroids"
        ],
        "supportive_care": [
            "Avoid allergens",
            "Skin care management"
        ],
        "notes": "Allergic reaction causing skin irritation."
    },

    "Demodicosis": {
        "medication": [
            "Ivermectin",
            "Amitraz dips",
            "Topical selamectin"
        ],
        "supportive_care": [
            "Improve hygiene",
            "Immune system support"
        ],
        "notes": "Mite infestation affecting hair follicles."
    },

    "Ringworm": {
        "medication": [
            "Itraconazole",
            "Topical antifungal ointment"
        ],
        "supportive_care": [
            "Environmental disinfection",
            "Isolation if contagious"
        ],
        "notes": "Fungal infection that can spread to other animals or humans."
    }
}


# ==========================================
# IMAGE TREATMENT FUNCTION
# ==========================================

def get_image_treatment(predicted_disease: str) -> dict:
    """
    Returns diagnosis and treatment for diseases predicted
    by the image diagnosis model.
    """

    if not predicted_disease:
        return {
            "error": "No disease provided."
        }

    if predicted_disease not in IMAGE_TREATMENT_DB:
        return {
            "warning": f"No treatment found for {predicted_disease}.",
            "suggestion": "Consult a veterinarian."
        }

    treatment_info = IMAGE_TREATMENT_DB[predicted_disease]

    return {
        "disease": predicted_disease,
        "medication": treatment_info["medication"],
        "supportive_care": treatment_info["supportive_care"],
        "notes": treatment_info["notes"]
    }





