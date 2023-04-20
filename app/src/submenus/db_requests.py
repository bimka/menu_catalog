import uuid

from .schemas import SubmenuCreate
from ..models import Menu, Submenu


class SubmenuDB:
    def __init__(self, db):
        self.db = db

    def get_submenus(self):
        return self.db.query(Submenu).all()

    def create_submenu(self, menu_id: uuid.UUID, submenu: SubmenuCreate):
        new_submenu = Submenu(title=submenu.title,
                              description=submenu.description,
                              menu_id=menu_id)
        self.db.add(new_submenu)
        self.db.flush()
        menu: Menu = self.db.query(Menu) \
                         .filter(Menu.id == menu_id) \
                         .first()
        menu.submenus_count += 1
        self.db.commit()
        return new_submenu

    def get_submenu_by_title(self, title):
        return self.db.query(Submenu) \
                   .filter(Submenu.title == title) \
                   .first()

    def get_submenu_by_id(self, submenu_id: uuid.UUID):
        return self.db.query(Submenu) \
                   .filter(Submenu.id == submenu_id) \
                   .first()

    def delete_submenu(self, menu_id: uuid, submenu_id: uuid.UUID):
        submenu_db = self.db.query(Submenu) \
                         .filter(Submenu.id == submenu_id) \
                         .first()
        self.db.delete(submenu_db)
        self.db.flush()
        menu: Menu = self.db.query(Menu) \
                         .filter(Menu.id == menu_id) \
                         .first()
        menu.submenus_count -= 1
        menu.dishes_count = 0
        self.db.commit()

    def update_submenu(self, submenu_id: uuid.UUID, submenu: dict):
        if submenu.get("title"):
            new_title = submenu["title"]
            self.db.query(Submenu) \
                .filter(Submenu.id == submenu_id) \
                .update({'title': new_title})

        if submenu["description"]:
            new_description = submenu["description"]
            self.db.query(Submenu) \
                .filter(Submenu.id == submenu_id) \
                .update({'description': new_description})

        self.db.commit()
        return self.get_submenu_by_id(submenu_id)
