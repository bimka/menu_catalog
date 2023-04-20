from fastapi import Depends
from sqlalchemy.orm import Session

from .db_requests import SubmenuDB
from .service import SubmenuService
from ..session import get_db


def get_submenuDB(db: Session = Depends(get_db)):
    return SubmenuDB(db)


def get_submenu_service(submenuDB: SubmenuDB = Depends(get_submenuDB)):
    return SubmenuService(submenuDB)


