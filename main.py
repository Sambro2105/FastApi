import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000, log_level="debug", reload=True)
