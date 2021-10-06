from pydantic import BaseModel

from schemas.blog.blog import Blog


class ShowUser(BaseModel):
    id: int
    username: str
    blogs: list[Blog] = []

    class Config:
        orm_mode = True
