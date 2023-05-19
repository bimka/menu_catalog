from fastapi import Depends
from sqlalchemy.orm import Session

from .db_requests import DishDB
from .service import DishService
from ..session import get_db
from ..cache import Cache, get_cache


def get_dish_db(db: Session = Depends(get_db)):
    return DishDB(db)


def get_dish_service(
    dish_db: DishDB = Depends(get_dish_db), cache: Cache = Depends(get_cache)
):
    return DishService(dish_db, cache)
