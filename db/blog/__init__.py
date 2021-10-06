from .base import Base
from .engine import engine
from .get_db import get_db
from .models import *
from .session import SessionLocal


def init_db():
    Base.metadata.create_all(bind=engine)
