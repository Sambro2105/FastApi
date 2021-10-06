from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import utils
from api.v1 import oauth
from db.blog import get_db, models


def login(request: OAuth2PasswordRequestForm, db: Session = Depends(get_db)):
    """
    Loges in user.
    """
    user = (
        db.query(models.User).filter(models.User.username == request.username).first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with username = "{request.username}" not found.',
        )

    if not utils.Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )

    access_token = oauth.create_access_token(
        data={"id": user.id, "username": user.username},
    )

    return {"access_token": access_token, "token_type": "bearer"}
