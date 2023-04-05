import uuid

from sqlalchemy.orm import Session

from src.dishes import db_requests, schemas


def create_dish(menu_id: uuid.UUID,
                submenu_id: uuid.UUID,
                dish: schemas.DishCreate,
                db: Session):
    dish_in_db = db_requests.get_dish_by_title(dish.title, db)
    if dish_in_db:
        return None
    return db_requests.create_dish(menu_id, submenu_id, dish, db)


def get_dishes(db: Session):
    return db_requests.get_dishes(db)


def get_dish(dish_id: uuid.UUID, db: Session):
    dish_in_db = db_requests.get_dish_by_id(dish_id, db)
    if not dish_in_db:
        return None
    return dish_in_db


def delete_dish(menu_id: uuid.UUID,
                submenu_id: uuid.UUID,
                dish_id: uuid.UUID,
                db: Session):
    dish_in_db = db_requests.get_dish_by_id(dish_id, db)
    if not dish_in_db:
        return None
    db_requests.delete_dish(menu_id, submenu_id, dish_id, db)
    return 1


def update_dish(dish_id: uuid.UUID,
                dish: dict,
                db: Session):

    dish_in_db = db_requests.get_dish_by_id(dish_id, db)
    if not dish_in_db:
        return -1

    if dish.get("title"):
        new_title = dish["title"]
        dish_in_db = db_requests.get_dish_by_title(new_title, db)
        if dish_in_db:
            return 0

    return db_requests.update_dish(dish_id, dish, db)