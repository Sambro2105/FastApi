from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import schemas
from api.v1 import oauth
from db.blog import get_db
from . import actions

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create_blog(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_user),
):
    """
    Creates blog.
    """
    return actions.create_blog(request, db, current_user)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.ShowBlog])
def get_all_blogs(
    db: Session = Depends(get_db),
):
    """
    Returns all blogs.
    """
    return actions.get_all_blogs(db)


@router.get(
    "/{blog_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog
)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    """
    Returns blog by id.
    """
    return actions.get_blog(blog_id, db)


@router.delete("/{blog_id}", status_code=status.HTTP_200_OK)
def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_user),
):
    """
    Deletes blog by id.
    """
    return actions.delete_blog(blog_id, db, current_user)


@router.put("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(
    request: schemas.Blog,
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(oauth.get_current_user),
):
    """
    Updates blog by id.
    """
    return actions.update_blog(request, blog_id, db, current_user)
