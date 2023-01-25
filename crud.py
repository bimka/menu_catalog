from sqlalchemy.orm import Session

import models, schemas


def get_menu(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_menu_by_title(db: Session, title: str):
    return db.query(models.Menu).filter(models.Menu.title == title).first()


def get_menus(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(title=menu.title, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

 
def delete_menu(db: Session, menu_id: int):
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
    



    
