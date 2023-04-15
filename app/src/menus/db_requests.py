import uuid

from sqlalchemy.orm import Session

from .. import models
from . import schemas


def create_menu(menu: schemas.MenuCreate, db: Session):
    new_menu = models.Menu(title=menu.title,
                           description=menu.description)
    db.add(new_menu)
    db.commit()
    return new_menu


def get_menus(db: Session):
    return db.query(models.Menu).all()


def get_menu_by_id(menu_id: uuid, db: Session):
    return db.query(models.Menu)\
             .filter(models.Menu.id == menu_id)\
             .first()


def get_menu_by_title(title: str, db: Session):
    return db.query(models.Menu)\
             .filter(models.Menu.title == title)\
             .first()


def delete_menu(menu_id: uuid.UUID, db: Session):
    menu_db = db.query(models.Menu)\
                .filter(models.Menu.id == menu_id)\
                .first()
    db.delete(menu_db)
    db.commit()


def update_menu(menu_id: uuid.UUID, menu: dict, db: Session):
    if menu.get("title"):
        new_title = menu["title"]
        db.query(models.Menu)\
            .filter(models.Menu.id == menu_id)\
            .update({'title': new_title})

    if menu["description"]:
        new_description = menu["description"]
        db.query(models.Menu)\
            .filter(models.Menu.id == menu_id)\
            .update({'description': new_description})

    db.commit()
    return get_menu_by_id(menu_id, db)


