from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.blog import models


def get_user(user_id: int, db: Session):
    """
    Returns user by id.
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id = "{user_id}" not found.',
        )

    return user
