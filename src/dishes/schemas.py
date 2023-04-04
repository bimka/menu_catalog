import uuid

from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class Dish(DishBase):
    id: int
    submenu_id: int
    menu_id: uuid.UUID

    class Config:
        orm_mode = True


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    pass
