import uvicorn
from fastapi import FastAPI

import api
from db.blog import init_db

tags_metadata = [
    {
        "name": "Blogs",
        "description": "Operations with blogs.",
    },
    {
        "name": "Users",
        "description": "Operations with users.",
    },
    {
        "name": "Auth",
        "description": "Operations with authentication.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(api.router, prefix="/api")

if __name__ == "__main__":
    init_db()
    uvicorn.run(
        app="main:app", host="localhost", port=8000, log_level="debug", reload=True
    )
