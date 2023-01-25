from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/menus/", status_code=status.HTTP_201_CREATED)
def create_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    db_menu = crud.get_menu_by_title(db, title=menu.title)
    if db_menu:
        raise HTTPException(status_code=400, 
                            detail="Menu with this name already exists")
    return crud.create_menu(db=db, menu=menu)


@app.get("/api/v1/menus/", response_model=list[schemas.Menu])
def read_menus(db: Session = Depends(get_db)):
    return crud.get_menus(db)


@app.get("/api/v1/menus/{menu_id}", response_model=schemas.Menu)
def read_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return db_menu


@app.delete("/api/v1/menus/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return crud.delete_menu(db=db, menu_id=menu_id)


@app.patch("/api/v1/menus/{menu_id}", response_model=schemas.Menu)
def update_menu(menu_id: int, 
                menu: schemas.MenuUpdate, 
                db: Session = Depends(get_db)):
    db_menu = crud.get_menu(db, menu_id=menu_id)
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    menu_data = menu.dict(exclude_unset=True)
    return crud.update_menu(db=db, db_menu=db_menu, menu_data=menu_data)

