from schemas.blog.base_blog import BaseBlog


class Blog(BaseBlog):
    class Config:
        orm_mode = True
