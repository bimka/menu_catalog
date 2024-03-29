import json
import uuid

from fastapi.encoders import jsonable_encoder

from .db_requests import MenuDB
from .schemas import MenuCreate
from ..cache import Cache


class MenuService:
    def __init__(self, menu_db: MenuDB, cache: Cache):
        self.menuDB = menu_db
        self.cache = cache

    def get_menus(self):
        menu_list = self.cache.get("menu_list:")
        if menu_list is None:
            menu_list = self.menuDB.get_menus()
            menu_str_list = json.dumps(jsonable_encoder(menu_list))
            self.cache.set("menu_list:", menu_str_list)
        return menu_list

    def create_menu(self, menu: MenuCreate):
        menu_in_db = self.menuDB.get_menu_by_title(menu.title)
        if menu_in_db:
            return None
        menu_str = json.dumps(jsonable_encoder(menu))
        self.cache.append("menu_list:", menu_str)
        return self.menuDB.create_menu(menu)

    def get_menu(self, menu_id: uuid):
        cashed_data = self.cache.get(f"menu_{menu_id}:")
        if cashed_data:
            db_menu = cashed_data
        else:
            db_menu = self.menuDB.get_menu_by_id(menu_id)
            if not db_menu:
                return None
            menu_str = json.dumps(jsonable_encoder(db_menu))
            self.cache.set(f"menu_{menu_id}:", menu_str)
        return db_menu

    def delete_menu(self, menu_id: uuid.UUID):
        menu_in_db = self.menuDB.get_menu_by_id(menu_id)
        if not menu_in_db:
            return None
        self.menuDB.delete_menu(menu_id)
        self.cache.delete(f"menu_{menu_id}:")
        self.cache.delete("menu_list:")
        return 1

    def update_menu(self, menu_id: uuid.UUID, menu: dict):
        menu_in_db = self.menuDB.get_menu_by_id(menu_id)
        if not menu_in_db:
            return -1

        if menu.get("title"):
            new_title = menu["title"]
            menu_in_db = self.menuDB.get_menu_by_title(new_title)
            if menu_in_db:
                return 0
        self.cache.delete(f"menu_{menu_id}:")
        return self.menuDB.update_menu(menu_id, menu)
