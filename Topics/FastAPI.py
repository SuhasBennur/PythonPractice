# app_fastapi.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name} from FastAPI!"}

##run with -> uvicorn app_fastapi:app --reload --port 8000