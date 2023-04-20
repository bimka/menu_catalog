from fastapi import Depends
from sqlalchemy.orm import Session

from .db_requests import MenuDB
from .service import MenuService
from ..session import get_db


def get_menuDB(db: Session = Depends(get_db)):
    return MenuDB(db)


def get_menu_service(menuDB: MenuDB = Depends(get_menuDB)):
    return MenuService(menuDB)


