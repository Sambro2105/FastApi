from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import schemas
from db.blog import models


def update_blog(
    request: schemas.Blog,
    blog_id: int,
    db: Session,
    current_user: schemas.TokenData,
):
    """
    Updates blog by id.
    """
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

    blog_data = blog.first()

    if not blog_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id = {blog_id} not found.",
        )

    if not blog_data.user_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Can only update one's own blogs",
        )

    blog.update({models.Blog.title: request.title, models.Blog.body: request.body})
    db.commit()
    return blog.first()
