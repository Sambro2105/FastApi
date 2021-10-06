from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import schemas
from db.blog import get_db
from . import actions

router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.Token)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    """
    Loges in user.
    """
    return actions.login(request, db)


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser
)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    """
    Creates user.
    """
    return actions.register(request, db)
