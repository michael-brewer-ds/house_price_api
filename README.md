# House Price Prediction API

A FastAPI service that loads a trained scikit-learn regression model and returns house price predictions from 13 property features.

The project demonstrates how a machine learning model can be packaged behind a web API with input validation, model metadata, health checks, and interactive API documentation.

## Features

- Loads the trained model once when the application starts
- Validates prediction requests with Pydantic
- Returns predictions in a consistent response format
- Provides model metadata through a dedicated endpoint
- Reports model and service status through a health endpoint
- Generates interactive documentation with FastAPI and Swagger UI

## Project Structure

```text
house_price_api/
├── api.py                 # Model loading, prediction, and health logic
├── main.py                # FastAPI application and route definitions
├── schemas.py             # Request and response validation models
├── model.pkl              # Trained scikit-learn model
└── model_metadata.json    # Model version, features, and evaluation details
```

## Requirements

- Python 3.9 or newer
- FastAPI
- Uvicorn
- Pydantic
- NumPy
- joblib
- scikit-learn

## Run Locally

### 1. Open the project

Open the `house_price_api` folder in Visual Studio Code.

### 2. Create a virtual environment

Open the Visual Studio Code terminal and run:

```bash
python3 -m venv venv
```

On Windows, use `python` instead of `python3` if needed.

### 3. Activate the virtual environment

macOS or Linux:

```bash
source venv/bin/activate
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install fastapi uvicorn pydantic numpy joblib scikit-learn
```

### 5. Start the API

With the virtual environment active, run this command in the Visual Studio Code terminal:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

The `--reload` option automatically restarts the development server when Python source files change.

## API Documentation

Open the interactive Swagger documentation in a browser:

```text
http://127.0.0.1:8000/docs
```

The OpenAPI specification is also available at:

```text
http://127.0.0.1:8000/openapi.json
```

## Endpoints

### `GET /`

Returns basic information about the API and its available endpoints.

### `GET /health`

Confirms whether the service and model are ready. A successful response reports:

```json
{
  "status": "healthy",
  "model_loaded": true,
  "message": "Service is running and model is loaded"
}
```

### `GET /model/info`

Returns the model type, version, training date, feature order, RMSE, and description.

### `POST /predict`

Accepts property information and returns a predicted price. The request must include these 13 fields:

- `total_images`
- `beds`
- `baths`
- `area`
- `latitude`
- `longitude`
- `garden`
- `garage`
- `new_construction`
- `pool`
- `terrace`
- `air_conditioning`
- `parking`

Example request:

```json
{
  "total_images": 10,
  "beds": 3,
  "baths": 2.5,
  "area": 1800.0,
  "latitude": 40.7128,
  "longitude": -74.0060,
  "garden": 1,
  "garage": 1,
  "new_construction": 0,
  "pool": 0,
  "terrace": 1,
  "air_conditioning": 1,
  "parking": 1
}
```

Example response:

```json
{
  "predicted_price": 480032.65,
  "currency": "USD",
  "model_version": "1.0.0"
}
```

## Notes

The `model.pkl` file was created with scikit-learn and must remain in the project folder so the API can load it at startup. Package versions can affect serialized models, so use a compatible scikit-learn version if the model-loading warning recommends one.

When creating a submission archive, include the Python files, `model.pkl`, `model_metadata.json`, and this README. Do not include `venv`, `__pycache__`, `.DS_Store`, or server log files.
