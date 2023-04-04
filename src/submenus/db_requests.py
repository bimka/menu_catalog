import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

import src
from src import models, menus
from src.session import get_db
from src.submenus import schemas


def create_submenu(menu_id: uuid.UUID, submenu: schemas.SubmenuCreate, db: Session):
    new_submenu = models.Submenu(title=submenu.title,
                                 description=submenu.description,
                                 menu_id=menu_id)
    db.add(new_submenu)
    db.flush()
    menu: models.Menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    menu.submenus_count += 1
    # menus.db_requests.add_one_submenu_to_the_submenus_count(new_submenu.menu_id, db)
    db.commit()
    return new_submenu


def get_submenus(db: Session):
    return db.query(models.Submenu).all()


def get_submenu_by_id(submenu_id: uuid, db: Session):
    return db.query(models.Submenu).get(submenu_id)


def get_submenu_by_title(title: str, db: Session):
    return db.query(models.Submenu).filter(models.Submenu.title == title).first()


def get_count_of_submenus(title: str, db: Session) -> int:
    return db.query(models.Submenu)\
        .filter(models.Submenu.title == title)\
        .count()


def delete_submenu(menu_id: uuid.UUID, submenu_id: int, db: Session):
    submenu_db = db.query(models.Submenu)\
                                .filter(models.Submenu.id == submenu_id)\
                                .first()
    db.delete(submenu_db)
    menu: models.Menu = db.query(models.Menu)\
                          .filter(models.Menu.id == menu_id)\
                          .first()
    menu.submenus_count += 1
    db.commit()
    return submenu_db


def update_submenu(submenu_id: uuid.UUID, submenu: dict, db: Session):
    if submenu.get("title"):
        new_title = submenu["title"]
        db.query(models.Submenu) \
            .filter(models.Submenu.id == submenu_id) \
            .update({'title': new_title})

    if submenu["description"]:
        new_description = submenu["description"]
        db.query(models.Submenu) \
            .filter(models.Submenu.id == submenu_id) \
            .update({'description': new_description})

    db.commit()
    return get_submenu_by_id(submenu_id, db)


# def add_one_dish_to_the_dishes_count(submenu_id: uuid.UUID, db: Session):
#     db.query(models.Submenu) \
#         .filter(models.Submenu.id == submenu_id) \
#         .update({"dishes_count": models.Submenu.dishes_count + 1})
#
#
# def reduce_one_dish_to_the_dishes_count(submenu_id: uuid.UUID, db: Session):
#     db.query(models.Submenu) \
#         .filter(models.Submenu.id == submenu_id) \
#         .update({"dishes_count": models.Submenu.dishes_count - 1})
