import uuid

from sqlalchemy.orm import Session

from src.submenus import db_requests, schemas


def create_submenu(menu_id: uuid.UUID,
                   submenu: schemas.SubmenuCreate,
                   db: Session):
    submenu_in_db = db_requests.get_submenu_by_title(submenu.title, db)
    if submenu_in_db:
        return None
    return db_requests.create_submenu(menu_id, submenu, db)


def get_submenus(db: Session):
    return db_requests.get_submenus(db)


def get_submenu(submenu_id: uuid, db: Session):
    submenu_in_db = db_requests.get_submenu_by_id(submenu_id, db)
    if not submenu_in_db:
        return None
    return submenu_in_db


def delete_submenu(menu_id: uuid.UUID, submenu_id: uuid.UUID, db: Session):
    submenu_in_db = db_requests.get_submenu_by_id(submenu_id, db)
    if not submenu_in_db:
        return None
    db_requests.delete_submenu(menu_id, submenu_id, db)
    return 1


def update_submenu(submenu_id: uuid.UUID,
                   submenu: dict,
                   db: Session):

    submenu_in_db = db_requests.get_submenu_by_id(submenu_id, db)
    if not submenu_in_db:
        return -1

    if submenu.get("title"):
        new_title = submenu["title"]
        submenu_in_db = db_requests.get_submenu_by_title(new_title, db)
        if submenu_in_db:
            return 0

    return db_requests.update_submenu(submenu_id, submenu, db)