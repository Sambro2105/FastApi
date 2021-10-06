from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import schemas
from db.blog import models


def delete_blog(blog_id: int, db: Session, current_user: schemas.TokenData):
    """
    Deletes blog by id.
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
            detail="Can only delete one's own blogs",
        )

    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": "done"}
