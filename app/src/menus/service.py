import uuid

from .db_requests import MenuDB
from .schemas import MenuCreate
from ..cache import Cache


class MenuService:
    def __init__(self, menuDB: MenuDB, cache: Cache):
        self.menuDB = menuDB
        self.cache = cache

    def get_menus(self):
        return self.menuDB.get_menus()

    def create_menu(self, menu: MenuCreate):
        menu_in_db = self.menuDB.get_menu_by_title(menu.title)
        if menu_in_db:
            return None
        return self.menuDB.create_menu(menu)

    def get_menu(self, menu_id: uuid):
        menu_in_db = self.menuDB.get_menu_by_id(menu_id)
        if not menu_in_db:
            return None
        return menu_in_db

    def delete_menu(self, menu_id: uuid.UUID):
        menu_in_db = self.menuDB.get_menu_by_id(menu_id)
        if not menu_in_db:
            return None
        self.menuDB.delete_menu(menu_id)
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

        return self.menuDB.update_menu(menu_id, menu)
