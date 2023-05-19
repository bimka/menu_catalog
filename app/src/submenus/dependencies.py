from fastapi import Depends
from sqlalchemy.orm import Session

from .db_requests import SubmenuDB
from .service import SubmenuService
from ..session import get_db
from ..cache import Cache, get_cache


def get_submenu_db(db: Session = Depends(get_db)):
    return SubmenuDB(db)


def get_submenu_service(
    submenu_db: SubmenuDB = Depends(get_submenu_db),
    cache: Cache = Depends(get_cache),
):
    return SubmenuService(submenu_db, cache)
