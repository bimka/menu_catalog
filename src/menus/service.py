import uuid

from sqlalchemy.orm import Session

from src.menus import db_requests, schemas


def create_menu(menu: schemas.MenuCreate, db: Session):
    menu_in_db = db_requests.get_menu_by_title(menu.title, db)
    if menu_in_db:
        return None
    return db_requests.create_menu(menu, db)


def get_menus(db: Session):
    return db_requests.get_menus(db)


def get_menu(menu_id: uuid, db: Session):
    menu_in_db = db_requests.get_menu_by_id(menu_id, db)
    if not menu_in_db:
        return None
    return menu_in_db


def delete_menu(menu_id: uuid, db: Session):

    menu_in_db = db_requests.get_menu_by_id(menu_id, db)
    if not menu_in_db:
        return None
    checking_menu_delete = db_requests.delete_menu(menu_id, db)
    return checking_menu_delete


def update_menu(menu_id: uuid.UUID,
                menu: dict,
                db: Session):

    menu_in_db = db_requests.get_menu_by_id(menu_id, db)
    if not menu_in_db:
        return -1

    if menu.get("title"):
        new_title = menu["title"]
        menu_in_db = db_requests.get_menu_by_title(new_title, db)
        if menu_in_db:
            return 0

    return db_requests.update_menu(menu_id, menu, db)