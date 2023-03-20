import uuid

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str
    submenus_count: int = 0
    dishes_count: int = 0


class Menu(MenuBase):
    id: uuid.UUID

    # submenus: list[Submenu] = []

    class Config:
        orm_mode = True

class MenuCreate(MenuBase):
    pass

class MenuUpdate(MenuBase):
    pass
