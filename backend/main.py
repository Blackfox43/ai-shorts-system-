from fastapi import FastAPI
from series.generator import generate_series

app = FastAPI()

@app.post("/generate")
def generate(payload: dict):
    return generate_series(payload)
