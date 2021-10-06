from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import schemas
from db.blog import models
from utils.hashing import Hash


def register(request: schemas.User, db: Session):
    """
    Creates a user.
    """
    user = (
        db.query(models.User).filter(models.User.username == request.username).first()
    )

    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'User with username = "{request.username}" already exists',
        )

    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(username=request.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
