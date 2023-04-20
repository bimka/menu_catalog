import uuid

from .db_requests import SubmenuDB
from .schemas import SubmenuCreate


class SubmenuService:
    def __init__(self, submenuDB: SubmenuDB):
        self.submenuDB = submenuDB

    def get_submenus(self):
        return self.submenuDB.get_submenus()

    def create_submenu(self, menu_id: uuid.UUID, submenu: SubmenuCreate):
        submenu_in_db = self.submenuDB.get_submenu_by_title(submenu.title)
        if submenu_in_db:
            return None
        return self.submenuDB.create_submenu(menu_id, submenu)

    def get_submenu(self, submenu_id: uuid.UUID):
        submenu_in_db = self.submenuDB.get_submenu_by_id(submenu_id)
        if not submenu_in_db:
            return None
        return submenu_in_db

    def delete_submenu(self, menu_id: uuid, submenu_id: uuid.UUID):
        submenu_in_db = self.submenuDB.get_submenu_by_id(submenu_id)
        if not submenu_in_db:
            return None
        self.submenuDB.delete_submenu(menu_id, submenu_id)
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

        return self.submenuDB.update_submenu(submenu_id, submenu)
