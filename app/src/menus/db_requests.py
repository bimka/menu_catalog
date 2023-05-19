import uuid

from .schemas import MenuCreate
from ..models import Menu


class MenuDB:
    def __init__(self, db):
        self.db = db

    def get_menus(self):
        return self.db.query(Menu).all()

    def create_menu(self, menu: MenuCreate):
        new_menu = Menu(title=menu.title, description=menu.description)
        self.db.add(new_menu)
        self.db.commit()
        return new_menu

    def get_menu_by_title(self, title):
        return self.db.query(Menu).filter(Menu.title == title).first()

    def get_menu_by_id(self, menu_id: uuid):
        return self.db.query(Menu).filter(Menu.id == menu_id).first()

    def delete_menu(self, menu_id: uuid.UUID):
        menu_db = self.db.query(Menu).filter(Menu.id == menu_id).first()
        self.db.delete(menu_db)
        self.db.commit()

    def update_menu(self, menu_id: uuid.UUID, menu: dict):
        if menu.get("title"):
            new_title = menu["title"]
            self.db.query(Menu).filter(Menu.id == menu_id).update(
                {"title": new_title}
            )

        if menu["description"]:
            new_description = menu["description"]
            self.db.query(Menu).filter(Menu.id == menu_id).update(
                {"description": new_description}
            )

        self.db.commit()
        return self.get_menu_by_id(menu_id)
