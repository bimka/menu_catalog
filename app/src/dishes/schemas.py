import uuid

from pydantic import BaseModel


class DishBase(BaseModel):
    title: str
    description: str
    price: str


class Dish(DishBase):
    id: uuid.UUID
    submenu_id: uuid.UUID
    menu_id: uuid.UUID

    class Config:
        orm_mode = True


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    pass
