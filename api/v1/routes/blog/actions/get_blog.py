from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.blog import models


def get_blog(blog_id: int, db: Session):
    """
    Returns blog by id.
    """
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id = {blog_id} not found.",
        )

    return blog
