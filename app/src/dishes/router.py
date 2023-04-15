import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from ..session import get_db
from . import schemas, service

dish_router = APIRouter()


@dish_router.post("/{menu_id}/submenus/{submenu_id}/dishes",
                  response_model=schemas.Dish,
                  status_code=status.HTTP_201_CREATED)
def create_dish(menu_id: uuid.UUID,
                submenu_id: uuid.UUID,
                dish: schemas.DishCreate,
                db: Session = Depends(get_db)):
    new_dish = service.create_dish(menu_id, submenu_id, dish, db)
    if new_dish is None:
        raise HTTPException(status_code=201, detail="Dish already exists.")
    return new_dish


@dish_router.get("/{menu_id}/submenus/{submenu_id}/dishes",
                 response_model=list[schemas.Dish])
def read_dishes(db: Session = Depends(get_db)):
    db_dishes = service.get_dishes(db)
    return db_dishes


@dish_router.get("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
                 response_model=schemas.Dish)
def read_dish(dish_id: uuid.UUID, db: Session = Depends(get_db)):
    db_dish = service.get_dish(dish_id, db)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="Dish is not found.")
    return db_dish


@dish_router.delete("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def delete_dish(menu_id: uuid.UUID,
                submenu_id: uuid.UUID,
                dish_id: uuid.UUID,
                db: Session = Depends(get_db)):
    db_dish_status = service.delete_dish(menu_id, submenu_id, dish_id, db)
    if db_dish_status is None:
        raise HTTPException(status_code=404, detail="Dish not found.")
    if db_dish_status == 1:
        return {"detail": "Dish is deleted successfully."}
    raise HTTPException(status_code=204, detail="Dish not deleted.")


@dish_router.patch("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}",
                   response_model=schemas.Dish)
def update_submenu(dish_id: uuid.UUID,
                   dish: dict,
                   db: Session = Depends(get_db)):
    db_dish = service.update_dish(dish_id, dish, db)
    if db_dish == -1:
        raise HTTPException(status_code=404, detail="Dish not found")
    if db_dish == 0:
        raise HTTPException(status_code=200, detail="Title is already exist.")

    return db_dish
