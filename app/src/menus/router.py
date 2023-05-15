import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from .dependencies import get_menu_service
from ..session import get_db
from . import schemas, service
from .service import MenuService

menu_router = APIRouter()


@menu_router.post("", response_model=schemas.Menu,
                  status_code=status.HTTP_201_CREATED)
def create_menu(menu: schemas.MenuCreate,
                menu_service: MenuService = Depends(get_menu_service)):
    new_menu = menu_service.create_menu(menu)
    if new_menu is None:
        raise HTTPException(status_code=400, detail="Menu already exists.")
    return new_menu


@menu_router.get("", response_model=list[schemas.Menu])
def read_menus(menu_service: MenuService = Depends(get_menu_service)):
    return menu_service.get_menus()


@menu_router.get("/{menu_id}", response_model=schemas.Menu)
def read_menu(menu_id: uuid.UUID,
              menu_service: MenuService = Depends(get_menu_service)):
    db_menu = menu_service.get_menu(menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu is not found.")
    return db_menu


@menu_router.delete("/{menu_id}")
def delete_menu(menu_id: uuid.UUID,
                menu_service: MenuService = Depends(get_menu_service)):
    db_menu_status = menu_service.delete_menu(menu_id)
    if db_menu_status is None:
        raise HTTPException(status_code=404, detail="Menu not found.")
    if db_menu_status == 1:
        return {"detail": "Menu is deleted successfully."}
    raise HTTPException(status_code=204, detail="Menu not deleted.")


@menu_router.patch("/{menu_id}", response_model=schemas.Menu)
def update_menu(menu_id: uuid.UUID,
                menu: dict,
                menu_service: MenuService = Depends(get_menu_service)):
    db_menu = menu_service.update_menu(menu_id, menu)
    if db_menu == -1:
        raise HTTPException(status_code=404, detail="Menu not found")
    if db_menu == 0:
        raise HTTPException(status_code=200, detail="Title is already exist.")
    return db_menu