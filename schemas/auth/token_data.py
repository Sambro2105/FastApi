from typing import Optional

from pydantic import BaseModel


class TokenData(BaseModel):
    id: int
    username: Optional[str] = None
