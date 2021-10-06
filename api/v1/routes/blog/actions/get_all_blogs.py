from sqlalchemy.orm import Session

from db.blog import models


def get_all_blogs(db: Session):
    """
    Returns all blogs.
    """
    return db.query(models.Blog).all()
