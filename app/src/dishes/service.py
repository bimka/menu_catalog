import json
import uuid

from fastapi.encoders import jsonable_encoder

from . import schemas
from .db_requests import DishDB
from ..cache import Cache


class DishService:
    def __init__(self, dish_db: DishDB, cache: Cache):
        self.dishDB = dish_db
        self.cache = cache

    def get_dishes(self):
        dishes_list = self.cache.get("dish_list:")
        if dishes_list is None:
            dishes_list = self.dishDB.get_dishes()
            dishes_str_list = json.dumps(jsonable_encoder(dishes_list))
            self.cache.set("dish_list:", dishes_str_list)
        return dishes_list

    def create_dish(
        self,
        menu_id: uuid.UUID,
        submenu_id: uuid.UUID,
        dish: schemas.DishCreate,
    ):
        dish_in_db = self.dishDB.get_dish_by_title(dish.title)
        if dish_in_db:
            return None
        dish_str = json.dumps(jsonable_encoder(dish))
        self.cache.append("dish_list:", dish_str)
        self.cache.delete(f"menu_{menu_id}:")
        self.cache.delete(f"submenu_{submenu_id}:")
        self.cache.delete("menu_list:")
        self.cache.delete("submenu_list:")
        return self.dishDB.create_dish(menu_id, submenu_id, dish)

    def get_dish(self, dish_id: uuid.UUID):
        cashed_data = self.cache.get(f"dish_{dish_id}:")
        if cashed_data:
            db_dish = cashed_data
        else:
            db_dish = self.dishDB.get_dish_by_id(dish_id)
            if not db_dish:
                return None
            dish_str = json.dumps(jsonable_encoder(db_dish))
            self.cache.set(f"dish_{dish_id}:", dish_str)
        return db_dish

    def delete_dish(
        self, menu_id: uuid.UUID, submenu_id: uuid.UUID, dish_id: uuid.UUID
    ):
        dish_in_db = self.dishDB.get_dish_by_id(
            dish_id,
        )
        if not dish_in_db:
            return None
        self.dishDB.delete_dish(menu_id, submenu_id, dish_id)
        self.cache.delete(f"dish_{dish_id}:")
        self.cache.delete(f"submenu_{submenu_id}:")
        self.cache.delete("submenu_list:")
        self.cache.delete("menu_list:")
        return 1

    def update_dish(self, dish_id: uuid.UUID, dish: dict):
        dish_in_db = self.dishDB.get_dish_by_id(dish_id)
        if not dish_in_db:
            return -1

        if dish.get("title"):
            new_title = dish["title"]
            dish_in_db = self.dishDB.get_dish_by_title(new_title)
            if dish_in_db:
                return 0

        return self.dishDB.update_dish(dish_id, dish)
