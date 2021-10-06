from sqlalchemy.orm import Session

import schemas
from db.blog import models


def create_blog(request: schemas.Blog, db: Session, current_user: schemas.TokenData):
    """
    Creates blog.
    """
    new_blog = models.Blog(
        title=request.title, body=request.body, user_id=current_user.id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
