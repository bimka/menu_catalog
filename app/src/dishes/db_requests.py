import uuid

from sqlalchemy.orm import Session

from .. import models
from . import schemas


def create_dish(menu_id: uuid.UUID,
                submenu_id: uuid.UUID,
                dish: schemas.DishCreate,
                db: Session):
    new_dish = models.Dish(title=dish.title,
                           description=dish.description,
                           price=dish.price,
                           menu_id=menu_id,
                           submenu_id=submenu_id)
    db.add(new_dish)
    db.flush()
    menu: models.Menu = db.query(models.Menu) \
        .filter(models.Menu.id == menu_id) \
        .first()
    submenu: models.Menu = db.query(models.Submenu) \
        .filter(models.Submenu.id == submenu_id) \
        .first()
    # menu: models.Menu = app.src.menus.db_requests.get_menu_by_id(menu_id, db)
    # submenu: models.Submenu = app.src.submenus.db_requests \
    #     .get_submenu_by_id(submenu_id, db)
    menu.dishes_count += 1
    submenu.dishes_count += 1
    db.commit()
    return new_dish


def get_dishes(db: Session):
    return db.query(models.Dish).all()


def get_dish_by_id(dish_id: uuid.UUID, db: Session):
    return db.query(models.Dish)\
             .filter(models.Dish.id == dish_id)\
             .first()


def get_dish_by_title(title: str, db: Session):
    return db.query(models.Dish)\
             .filter(models.Dish.title == title)\
             .first()


def delete_dish(menu_id: uuid.UUID,
                submenu_id: uuid.UUID,
                dish_id: uuid.UUID,
                db: Session):
    checking_dish_delete = db.query(models.Dish)\
                             .filter(models.Dish.id == dish_id)\
                             .delete()
    # menu: models.Menu = app.src.menus.db_requests.get_menu_by_id(menu_id, db)
    # submenu: models.Submenu = app.src.submenus.db_requests \
    #     .get_submenu_by_id(submenu_id, db)
    menu: models.Menu = db.query(models.Menu) \
        .filter(models.Menu.id == menu_id) \
        .first()
    submenu: models.Menu = db.query(models.Submenu) \
        .filter(models.Submenu.id == submenu_id) \
        .first()
    menu.dishes_count -= 1
    submenu.dishes_count -= 1
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

