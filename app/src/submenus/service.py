import json
import uuid

from fastapi.encoders import jsonable_encoder

from .db_requests import SubmenuDB
from .schemas import SubmenuCreate
from ..cache import Cache


class SubmenuService:
    def __init__(self, submenu_db: SubmenuDB, cache: Cache):
        self.submenuDB = submenu_db
        self.cache = cache

    def get_submenus(self):
        submenu_list = self.cache.get("submenu_list:")
        if submenu_list is None:
            submenu_list = self.submenuDB.get_submenus()
            submenu_str_list = json.dumps(jsonable_encoder(submenu_list))
            self.cache.set("submenu_list:", submenu_str_list)
        return submenu_list

    def create_submenu(self, menu_id: uuid.UUID, submenu: SubmenuCreate):
        submenu_in_db = self.submenuDB.get_submenu_by_title(submenu.title)
        if submenu_in_db:
            return None
        submenu_str = json.dumps(jsonable_encoder(submenu))
        self.cache.append("submenu_list:", submenu_str)
        self.cache.delete(f"menu_{menu_id}:")
        self.cache.delete("menu_list:")
        return self.submenuDB.create_submenu(menu_id, submenu)

    def get_submenu(self, submenu_id: uuid.UUID):
        cashed_data = self.cache.get(f"submenu_{submenu_id}:")
        if cashed_data:
            db_submenu = cashed_data
        else:
            db_submenu = self.submenuDB.get_submenu_by_id(submenu_id)
            if not db_submenu:
                return None
            submenu_str = json.dumps(jsonable_encoder(db_submenu))
            self.cache.set(f"submenu_{submenu_id}:", submenu_str)
        return db_submenu

    def delete_submenu(self, menu_id: uuid, submenu_id: uuid.UUID):
        submenu_in_db = self.submenuDB.get_submenu_by_id(submenu_id)
        if not submenu_in_db:
            return None
        self.submenuDB.delete_submenu(menu_id, submenu_id)
        self.cache.delete(f"submenu_{submenu_id}:")
        self.cache.delete("submenu_list")
        self.cache.delete("menu_list")
        return 1

    def update_submenu(self, submenu_id: uuid.UUID, submenu: dict):
        submenu_in_db = self.submenuDB.get_submenu_by_id(submenu_id)
        if not submenu_in_db:
            return -1

        if submenu.get("title"):
            new_title = submenu["title"]
            submenu_in_db = self.submenuDB.get_submenu_by_title(new_title)
            if submenu_in_db:
                return 0
        self.cache.delete(f"submenu_{submenu_id}:")
        self.cache.delete("submenu_list")
        self.cache.delete("menu_list")
        return self.submenuDB.update_submenu(submenu_id, submenu)
