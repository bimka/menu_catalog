import uuid

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import models
from src.session import get_db
from src import submenus
from src.dishes import schemas


def create_dish(dish: schemas.DishCreate, db: Session):
    new_dish = models.Dish(title=dish.title,
                           description=dish.description,
                           price=dish.price)
    db.add(new_dish)
    db.flush()
    print(new_dish.submenu_id)
    submenus.db_requests.add_one_dish_to_the_quantity(new_dish.submenu_id, db)
    db.commit()
    return new_dish


def get_dishes(db: Session):
    return db.query(models.Dish).all()


def get_dish_by_id(dish_id: uuid, db: Session):
    return db.query(models.Dish).get(dish_id)


def get_dish_by_title(title: str, db: Session):
    return db.query(models.Dish).filter(models.Dish.title == title).first()


def get_count_of_dishes(title: str, db: Session) -> int:
    return db.query(models.Dish).filter(models.Dish.title == title).count()


def delete_dish(dish_id: uuid, db: Session):
    checking_dish_delete = db.query(models.Dish).filter(models.Dish.id == dish_id).delete()
    db.commit()
    return checking_dish_delete


def update_dish(dish_id: uuid.UUID, dish: dict, db: Session):

    if dish.get("title"):
        new_title = dish["title"]
        db.query(models.Dish) \
            .filter(models.Dish.id == dish_id) \
            .update({'title': new_title})

    if dish["description"]:
        new_description = dish["description"]
        db.query(models.Dish) \
            .filter(models.Dish.id == dish_id) \
            .update({'description': new_description})

    if dish["price"]:
        new_price = dish["price"]
        db.query(models.Dish) \
            .filter(models.Dish.id == dish_id) \
            .update({'price': new_price})

    db.commit()
    return get_dish_by_id(dish_id, db)

