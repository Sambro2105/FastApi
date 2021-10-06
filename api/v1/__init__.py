from fastapi import APIRouter

from .routes import blog, user, auth

router = APIRouter()
router.include_router(blog.router, prefix="/blog", tags=["Blogs"])
router.include_router(user.router, prefix="/user", tags=["Users"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
