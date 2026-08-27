import joblib
import numpy as np
import json
from typing import Dict, Any

# Global variable to store the loaded model
model = None
metadata = None


def load_model_and_metadata():
    """
    Load the trained model and metadata from disk.
    Returns True if successful, False if there's an error.
    """
    global model, metadata

    try:
        model = joblib.load('model.pkl')

        with open('model_metadata.json', 'r') as f:
            metadata = json.load(f)

        print("Model and metadata loaded successfully!")
        return True

    except Exception as e:
        print(f"Error loading model or metadata: {e}")
        return False


def make_prediction(house_features: Dict[str, Any]) -> float:
    """
    Make a price prediction for a single house.

    Args:
        house_features: Dictionary containing all 13 features

    Returns:
        Predicted price as a float
    """
    global model, metadata

    if model is None:
        raise ValueError("Model not loaded")

    feature_values = [house_features[feature]
                      for feature in metadata['features']]

    X = np.array(feature_values).reshape(1, -1)

    prediction = model.predict(X)[0]

    # Round to 2 decimal places for currency
    return round(float(prediction), 2)


def get_model_info() -> Dict[str, Any]:
    """
    Get information about the loaded model.

    Returns:
        Dictionary containing model metadata

    Raises:
        ValueError: If metadata is not loaded
    """
    global metadata

    if metadata is None:
        raise ValueError("Model metadata not loaded")

    return metadata


def check_health() -> Dict[str, Any]:
    """
    Check the health status of the service.

    Returns:
        Dictionary with health status information
    """
    global model, metadata

    model_loaded = model is not None
    metadata_loaded = metadata is not None

    if model_loaded and metadata_loaded:
        health_status = {
            "status": "healthy",
            "model_loaded": True,
            "message": "Service is running and model is loaded"
        }
    else:
        health_status = {
            "status": "unhealthy",
            "model_loaded": model_loaded,
            "message": "Model or metadata failed to load"
        }

    return health_status
