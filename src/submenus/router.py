import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.submenus import schemas, service
from src.session import get_db

submenu_router = APIRouter()


@submenu_router.post("/{menu_id}/submenus",
                     response_model=schemas.Submenu,
                     status_code=status.HTTP_201_CREATED)
def create_submenu(
        menu_id: uuid.UUID,
        submenu: schemas.SubmenuCreate,
        db: Session = Depends(get_db)
):
    new_submenu = service.create_submenu(menu_id, submenu, db)
    if new_submenu is None:
        raise HTTPException(status_code=201, detail="Submenu already exists.")
    return new_submenu


@submenu_router.get("/{menu_id}/submenus",
                    response_model=list[schemas.Submenu])
def read_submenus(db: Session = Depends(get_db)):
    db_submenus = service.get_submenus(db)
    return db_submenus


@submenu_router.get("/{menu_id}/submenus/{submenu_id}",
                    response_model=schemas.Submenu)
def read_submenu(submenu_id: uuid.UUID, db: Session = Depends(get_db)):
    db_submenu = service.get_submenu(submenu_id, db)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="submenu not found")
    return db_submenu


@submenu_router.delete("/{menu_id}/submenus/{submenu_id}")
def delete_submenu(menu_id: uuid.UUID,
                   submenu_id: uuid.UUID,
                   db: Session = Depends(get_db)):
    db_submenu_status = service.delete_submenu(menu_id, submenu_id, db)
    if db_submenu_status is None:
        raise HTTPException(status_code=404, detail="Submenu not found.")
    if db_submenu_status == 1:
        return {"detail": "Submenu is deleted successfully."}
    return HTTPException(status_code=204, detail="Submenu not deleted.")


@submenu_router.patch("/{menu_id}/submenus/{submenu_id}",
                      response_model=schemas.Submenu)
def update_submenu(submenu_id: uuid.UUID,
                   submenu: dict,
                   db: Session = Depends(get_db)):
    db_submenu = service.update_submenu(submenu_id, submenu, db)
    if db_submenu == -1:
        raise HTTPException(status_code=404, detail="Submenu not found")
    if db_submenu == 0:
        raise HTTPException(status_code=200, detail="Title is already exist.")

    return db_submenu
