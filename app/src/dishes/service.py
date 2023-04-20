import uuid

from . import schemas
from .db_requests import DishDB


class DishService:
    def __init__(self, dishDB: DishDB):
        self.dishDB = dishDB

    def create_dish(self, menu_id: uuid.UUID,
                    submenu_id: uuid.UUID,
                    dish: schemas.DishCreate):
        dish_in_db = self.dishDB.get_dish_by_title(dish.title)
        if dish_in_db:
            return None
        return self.dishDB.create_dish(menu_id, submenu_id, dish)

    def get_dishes(self):
        return self.dishDB.get_dishes()

    def get_dish(self, dish_id: uuid.UUID):
        dish_in_db = self.dishDB.get_dish_by_id(dish_id)
        if not dish_in_db:
            return None
        return dish_in_db

    def delete_dish(self, menu_id: uuid.UUID,
                    submenu_id: uuid.UUID,
                    dish_id: uuid.UUID):
        dish_in_db = self.dishDB.get_dish_by_id(dish_id,)
        if not dish_in_db:
            return None
        self.dishDB.delete_dish(menu_id, submenu_id, dish_id)
        return 1

    def update_dish(self, dish_id: uuid.UUID,
                    dish: dict):

        dish_in_db = self.dishDB.get_dish_by_id(dish_id)
        if not dish_in_db:
            return -1

        if dish.get("title"):
            new_title = dish["title"]
            dish_in_db = self.dishDB.get_dish_by_title(new_title)
            if dish_in_db:
                return 0

        return self.dishDB.update_dish(dish_id, dish)