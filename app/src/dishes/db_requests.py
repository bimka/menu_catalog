import uuid

from . import schemas
from ..models import Menu, Submenu, Dish


class DishDB:
    def __init__(self, db):
        self.db = db

    def create_dish(
        self,
        menu_id: uuid.UUID,
        submenu_id: uuid.UUID,
        dish: schemas.DishCreate,
    ):
        new_dish = Dish(
            title=dish.title,
            description=dish.description,
            price=dish.price,
            menu_id=menu_id,
            submenu_id=submenu_id,
        )
        self.db.add(new_dish)
        self.db.flush()
        menu: Menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        submenu: Submenu = (
            self.db.query(Submenu).filter(Submenu.id == submenu_id).first()
        )
        menu.dishes_count += 1
        submenu.dishes_count += 1
        self.db.commit()
        return new_dish

    def get_dishes(self):
        return self.db.query(Dish).all()

    def get_dish_by_id(self, dish_id: uuid.UUID):
        return self.db.query(Dish).filter(Dish.id == dish_id).first()

    def get_dish_by_title(self, title: str):
        return self.db.query(Dish).filter(Dish.title == title).first()

    def delete_dish(
        self, menu_id: uuid.UUID, submenu_id: uuid.UUID, dish_id: uuid.UUID
    ):
        checking_dish_delete = (
            self.db.query(Dish).filter(Dish.id == dish_id).delete()
        )
        menu: Menu = self.db.query(Menu).filter(Menu.id == menu_id).first()
        submenu: Submenu = (
            self.db.query(Submenu).filter(Submenu.id == submenu_id).first()
        )
        menu.dishes_count -= 1
        submenu.dishes_count -= 1
        self.db.commit()
        return checking_dish_delete

    def update_dish(self, dish_id: uuid.UUID, dish: dict):
        if dish.get("title"):
            new_title = dish["title"]
            self.db.query(Dish).filter(Dish.id == dish_id).update(
                {"title": new_title}
            )

        if dish["description"]:
            new_description = dish["description"]
            self.db.query(Dish).filter(Dish.id == dish_id).update(
                {"description": new_description}
            )

        if dish["price"]:
            new_price = dish["price"]
            self.db.query(Dish).filter(Dish.id == dish_id).update(
                {"price": new_price}
            )

        self.db.commit()
        return self.get_dish_by_id(dish_id)
