from sqlalchemy.orm import Session

import schemas
from src import models


################################
#
#             Menu
#
################################


def get_menu(db: Session, menu_id: str):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_menus(db: Session):
    return db.query(models.Menu).all()


def create_menu(menu: schemas.MenuCreate, db: Session):
    db_menu = models.Menu(
        title=menu.title,
        description=menu.description,
        submenus_count=menu.submenus_count,
        dishes_count=menu.dishes_count
        )
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

 
def delete_menu(db: Session, menu_id: str):
    db_menu = get_menu(db, menu_id)
    db.delete(db_menu)
    db.commit()
    return {"detail": f"{db_menu.title} has been deleted"}


def update_menu(db: Session, db_menu: schemas.Menu, menu_data: dict):
    for key, value in menu_data.items():
        setattr(db_menu, key, value)
    db. add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu
    

################################
#
#             Submenu
#
################################

    
def get_submenus(db: Session, submenu: schemas.Submenu):
    return db.query(models.Submenu).filter_by(id=submenu.menu_id).all()