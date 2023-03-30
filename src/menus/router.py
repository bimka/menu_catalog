import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.menus import schemas, service
from src.session import get_db
from src.submenus.router import submenu_router

menu_router = APIRouter()


@menu_router.post("", response_model=schemas.Menu,
             status_code=status.HTTP_201_CREATED)
def create_menu(
        menu: schemas.MenuCreate,
        db: Session = Depends(get_db)
):
    new_menu = service.create_menu(menu, db)
    if new_menu is None:
        raise HTTPException(status_code=400, detail="Menu already exists.")
    return new_menu


@menu_router.get("", response_model=list[schemas.Menu])
def read_menus(db: Session = Depends(get_db)):
    db_menus = service.get_menus(db)
    if db_menus is None:
        raise HTTPException(status_code=404, detail="No menu found.")
    return db_menus


@menu_router.get("/{menu_id}", response_model=schemas.Menu)
def read_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    db_menu = service.get_menu(menu_id, db)
    if db_menu is None:
        raise HTTPException(status_code=200, detail="menu not found")
    return db_menu


@menu_router.delete("/{menu_id}")
def delete_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    db_menu_status = service.delete_menu(menu_id, db)
    if db_menu_status is None:
        raise HTTPException(status_code=404, detail="Menu not found.")
    if db_menu_status == 1:
        return {"detail": "Menu is deleted successfully."}
    raise HTTPException(status_code=204, detail="Menu not deleted.")


@menu_router.patch("/{menu_id}", response_model=schemas.Menu)
def update_menu(menu_id: uuid.UUID,
                menu: dict,
                db: Session = Depends(get_db)):
    db_menu = service.update_menu(menu_id, menu, db)
    if db_menu == -1:
        raise HTTPException(status_code=404, detail="Menu not found")
    if db_menu == 0:
        raise HTTPException(status_code=200, detail="Title is already exist.")

    return db_menu
