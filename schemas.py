from typing import Optional
from pydantic import BaseModel


class STask(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
