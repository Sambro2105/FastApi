from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

import schemas
from db.blog import get_db
from . import actions

router = APIRouter()


@router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowUser
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Returns user by id.
    """
    return actions.get_user(user_id, db)
