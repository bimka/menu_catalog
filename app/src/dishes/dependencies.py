from fastapi import Depends
from sqlalchemy.orm import Session

from .db_requests import DishDB
from .service import DishService
from ..session import get_db


def get_dishDB(db: Session = Depends(get_db)):
    return DishDB(db)


def get_dish_service(dishDB: DishDB = Depends(get_dishDB)):
    return DishService(dishDB)


