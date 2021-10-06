from pydantic import BaseModel


class BaseBlog(BaseModel):
    title: str
    body: str
