from fastapi import APIRouter

import api.v1

router = APIRouter()
router.include_router(v1.router, prefix="/v1")
