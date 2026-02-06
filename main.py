from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "status": "running",
        "model": "Anupom",
        "version": "v2"
    }

@app.post("/ask")
def ask(data: Question):
    return {
        "answer": f"You asked: {data.question}"
    }
