# FitAI

FitAI er en AI fitness webapp bygget i Python.

## Teknologier

- FastAPI
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Mistral AI

## Funktioner

- BMI beregning
- AI chatbot
- Vægtgrafer
- CSV datalagring

## Start projekt

### Backend

uvicorn main:app --reload

### Frontend

streamlit run FitAi.py

### Kør med Docker Compose

start docker desktop op

docker compose up --build

gå til http://localhost:8501/

## kør unittest

$env:PYTHONPATH="." 
pytest

## linting

uv run ruff check . --fix

## type checking

uv run pyright