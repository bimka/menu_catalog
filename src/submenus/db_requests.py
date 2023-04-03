import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import models
from src.session import get_db

from src.submenus import schemas


def create_submenu(submenu: schemas.SubmenuCreate, db: Session):
    new_submenu = models.Submenu(title=submenu.title,
                                 description=submenu.description,
                                 dishes_count=submenu.dishes_count)
    db.add(new_submenu)
    db.commit()
    return new_submenu


def get_submenus(db: Session):
    return db.query(models.Submenu).all()


def get_submenu_by_id(submenu_id: uuid, db: Session):
    return db.query(models.Submenu).get(submenu_id)


def get_submenu_by_title(title: str, db: Session):
    return db.query(models.Submenu).filter(models.Submenu.title == title).first()


def get_count_of_submenus(title: str, db: Session) -> int:
    return db.query(models.Submenu).filter(models.Submenu.title == title).count()


def delete_submenu(submenu_id: uuid, db: Session):
    checking_submenu_delete = db.query(models.Submenu).filter(models.Submenu.id == submenu_id).delete()
    db.commit()
    return checking_submenu_delete


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


def add_one_dish_to_the_quantity(submenu_id: uuid.UUID, db: Session):
    print(submenu_id)
    new_count = db.query(models.Submenu.dishes_count) \
        .filter(models.Submenu.id == submenu_id) \
        .first()
    print(new_count)
    db.query(models.Submenu) \
        .filter(models.Submenu.id == submenu_id) \
        .update({"dishes_count": new_count})
