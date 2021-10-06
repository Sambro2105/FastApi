from pydantic import BaseModel


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True
