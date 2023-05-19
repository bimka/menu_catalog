from fastapi import Depends
from sqlalchemy.orm import Session

from .db_requests import MenuDB
from .service import MenuService
from ..session import get_db
from ..cache import Cache, get_cache


def get_menu_db(db: Session = Depends(get_db)):
    return MenuDB(db)


def get_menu_service(
    menu_db: MenuDB = Depends(get_menu_db), cache: Cache = Depends(get_cache)
):
    return MenuService(menu_db, cache)
