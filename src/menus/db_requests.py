import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import models
from src.session import get_db

from src.menus import schemas


def create_menu(menu: schemas.MenuCreate, db: Session):
    new_menu = models.Menu(title=menu.title,
                           description=menu.description)
    db.add(new_menu)
    db.commit()
    return new_menu


def get_menus(db: Session):
    return db.query(models.Menu).all()


def get_menu_by_id(menu_id: uuid, db: Session):
    return db.query(models.Menu).get(menu_id)


def get_menu_by_title(title: str, db: Session):
    return db.query(models.Menu).filter(models.Menu.title == title).first()


def get_count_of_menus(title: str, db: Session) -> int:
    return db.query(models.Menu).filter(models.Menu.title == title).count()


def check_ability_to_update_menu(menu_id, new_title, db):
    pass


def delete_menu(menu_id: uuid, db: Session):
    menu_db = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    db.delete(menu_db)
    db.commit()
    return menu_db


def update_menu(menu_id: uuid.UUID, menu: dict, db: Session):
    if menu.get("title"):
        new_title = menu["title"]
        db.query(models.Menu) \
            .filter(models.Menu.id == menu_id) \
            .update({'title': new_title})

    if menu["description"]:
        new_description = menu["description"]
        db.query(models.Menu) \
            .filter(models.Menu.id == menu_id) \
            .update({'description': new_description})

    db.commit()
    return get_menu_by_id(menu_id, db)


# def add_one_submenu_to_the_submenus_count(menu_id: uuid.UUID, db: Session):
#     db.query(models.Menu) \
#         .filter(models.Menu.id == menu_id) \
#         .update({"submenus_count": models.Menu.submenus_count + 1})
#
#
# def reduce_one_submenu_to_the_submenus_count(menu_id: uuid.UUID, db: Session):
#     db.query(models.Submenu) \
#         .filter(models.Menu.id == menu_id) \
#         .update({"submenus_count": models.Menu.submenus_count - 1})

