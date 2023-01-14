from sqlalchemy.orm import Session

from . import models, schemas


def get_menu(db: Session, menu_id: int):
    return db.query(models.Menu).filter(models.Menu.id == menu_id).first()


def get_menus(db: Session):
    return db.query(models.Menu).all()


def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(name=menu.name)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

    
