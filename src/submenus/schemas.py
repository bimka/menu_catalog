import uuid

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str


class Submenu(SubmenuBase):
    id: int
    dishes_count: int = 0

    class Config:
        orm_mode = True


class SubmenuCreate(SubmenuBase):
    pass


class SubmenuUpdate(SubmenuBase):
    pass
