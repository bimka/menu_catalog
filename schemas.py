from pydantic import BaseModel


class FoodBase(BaseModel):
    name: str
    price: float


class FoodCreate(FoodBase):
    pass


class Food(FoodBase):
    id: int
    submenu_id: int


class SubmenuBase(BaseModel):
    name: str


class SubmenuCreate(SubmenuBase):
    pass 


class Submenu(SubmenuBase):
    id: int
    foods: list[Food] = []
    menu_id: int

    class Config:
        orm_mode = True


class MenuBase(BaseModel):
    name: str


class MenuCreate(MenuBase):
    pass 


class Menu(MenuBase):
    id: int
    submenus: list[Submenu] = []

    class Config:
        orm_mode = True












