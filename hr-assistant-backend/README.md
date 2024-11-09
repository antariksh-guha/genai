# Run and Debug Backend Locally

## Available Scripts

In the project directory, you can run:

### `Navigate to Project Directory`

cd hr-assistant-backend

### `Create Virtual Environment`

python -m venv venv

### `Activate Virtual Environment`

.\venv\Scripts\activate

### `Install Dependencies`

pip install -r requirements.txt

### `Run Backend`

python backend.py

### `Or with Uvicorn`

uvicorn backend:app --reload --port 8080

### `Test Health Endpoint`

curl http://localhost:8080/health