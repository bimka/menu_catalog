from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/menus/", response_model=schemas.Menu)
def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, name=menu.name)
    if db_menu:
        raise HTTPException(status_code=400, 
                            detail="Menu with this name already exists")
    return crud.create_menu(db=db, menu=menu)


@app.get("/menus/", response_model=list[schemas.Menu])
def read_menus(db: Session = Depends(get_db)):
    menus = crud.get_menus(db)
    return menus


@app.get("/menus/{user_id}", response_model=schemas.Menu)
def read_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return db_menu


