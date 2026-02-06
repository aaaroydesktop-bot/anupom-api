from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "running",
        "model": "Anupom",
        "created_by": "Anupom"
    }
