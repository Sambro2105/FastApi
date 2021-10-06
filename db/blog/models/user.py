from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.blog import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="user")
