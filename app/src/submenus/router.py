import uuid

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from .dependencies import get_submenu_service
from .service import SubmenuService
from ..session import get_db
from . import schemas, service

submenu_router = APIRouter()


@submenu_router.post("/{menu_id}/submenus",
                     response_model=schemas.Submenu,
                     status_code=status.HTTP_201_CREATED)
def create_submenu(
        menu_id: uuid.UUID,
        submenu: schemas.SubmenuCreate,
        submenu_service: SubmenuService = Depends(get_submenu_service)):
    new_submenu = submenu_service.create_submenu(menu_id, submenu)
    if new_submenu is None:
        raise HTTPException(status_code=201, detail="Submenu already exists.")
    return new_submenu


@submenu_router.get("/{menu_id}/submenus",
                    response_model=list[schemas.Submenu])
def read_submenus(submenu_service: SubmenuService = Depends(get_submenu_service)):
    db_submenus = submenu_service.get_submenus()
    return db_submenus


@submenu_router.get("/{menu_id}/submenus/{submenu_id}",
                    response_model=schemas.Submenu)
def read_submenu(submenu_id: uuid.UUID,
                 submenu_service: SubmenuService = Depends(get_submenu_service)):
    db_submenu = submenu_service.get_submenu(submenu_id)
    if db_submenu is None:
        raise HTTPException(status_code=404, detail="Submenu is not found.")
    return db_submenu


@submenu_router.delete("/{menu_id}/submenus/{submenu_id}")
def delete_submenu(menu_id: uuid.UUID,
                   submenu_id: uuid.UUID,
                   submenu_service: SubmenuService = Depends(get_submenu_service)):
    db_submenu_status = submenu_service.delete_submenu(menu_id, submenu_id)
    if db_submenu_status is None:
        raise HTTPException(status_code=404, detail="Submenu not found.")
    if db_submenu_status == 1:
        return {"detail": "Submenu is deleted successfully."}
    return HTTPException(status_code=204, detail="Submenu not deleted.")


@submenu_router.patch("/{menu_id}/submenus/{submenu_id}",
                      response_model=schemas.Submenu)
def update_submenu(submenu_id: uuid.UUID,
                   submenu: dict,
                   submenu_service: SubmenuService = Depends(get_submenu_service)):
    db_submenu = submenu_service.update_submenu(submenu_id, submenu)
    if db_submenu == -1:
        raise HTTPException(status_code=404, detail="Submenu not found")
    if db_submenu == 0:
        raise HTTPException(status_code=200, detail="Title is already exist.")

    return db_submenu
