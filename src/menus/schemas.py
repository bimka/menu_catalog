import uuid

from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str


class Menu(MenuBase):
    id: uuid.UUID
    submenus_count: int = 0
    dishes_count: int = 0

    class Config:
        orm_mode = True


class MenuCreate(MenuBase):
    pass

class MenuUpdate(MenuBase):
    pass
