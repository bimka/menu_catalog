import uuid

from pydantic import BaseModel


"""class FoodBase(BaseModel):
    name: str
    price: float


class FoodCreate(FoodBase):
    pass


class Food(FoodBase):
    id: int
    submenu_id: int

"""
################################
#
#             Submenu
#
#################################


class SubmenuBase(BaseModel):
    title: str
    description: str | None = None


class Submenu(SubmenuBase):
    id: uuid.UUID
    dishes_count: int
    #foods: list[Food] = []
    menu_id: int

    class Config:
        orm_mode = True


class SubmenuCreate(SubmenuBase):
    pass 


class SubmenuUpdate(BaseModel):
    title: str | None
    description: str | None


################################
#
#             Menu
#
#################################













