# Iris Classifier API with Flask & Docker

This project exposes a machine learning model trained on the Iris dataset as a RESTful API using Flask. The service is containerized using Docker, making it easy to deploy and run consistently across environments.

## Features

- Predicts Iris flower species from sepal and petal measurements.
- Flask-based REST API with a `/predict` endpoint.
- Dockerized for consistent deployment.
- Accepts JSON input and returns prediction as JSON.

## Model

The model is trained using `scikit-learn` classifiers such as:

- `DecisionTreeClassifier`
- `RandomForestClassifier`

Saved as a pickle file (`model.pkl`) and loaded by the Flask app.

## Project Structure

```
iris-flask-docker/
│
├── app.py                  # Main Flask application
├── model.pkl               # Trained ML model (serialized)
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
└── README.md               # Project documentation
```

## Installation (Local)

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the API:

   ```bash
   python app.py
   ```

3. Visit: `http://127.0.0.1:5000`

## Run with Docker

1. Build the Docker image:

   ```bash
   docker build -t iris-api .
   ```

2. Run the container:

   ```bash
   docker run -p 5000:5000 iris-api
   ```

3. The API is now available at: `http://127.0.0.1:5000`

## API Usage

**Endpoint**: `/predict`  
**Method**: `POST`  
**Content-Type**: `application/json`

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"
```

### Example Response

```json
{
  "prediction": "setosa"
}
```

## Requirements

- Python 3.8+
- Flask
- scikit-learn
- Docker (optional for containerized deployment)

## License

This is just my self-project 
This project is open-source and free to use for educational or personal purposes.
