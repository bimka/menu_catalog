import uuid

from pydantic import BaseModel


class SubmenuBase(BaseModel):
    title: str
    description: str
    dishes_count: int = 0


class Submenu(SubmenuBase):
    id: uuid.UUID

    # submenus: list[Submenu] = []

    class Config:
        orm_mode = True


class SubmenuCreate(SubmenuBase):
    pass


class SubmenuUpdate(SubmenuBase):
    pass
