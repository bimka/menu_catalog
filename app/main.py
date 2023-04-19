import uvicorn
from fastapi import FastAPI

from app.src.menus.router import menu_router
from app.src.submenus.router import submenu_router
from app.src.dishes.router import dish_router

app = FastAPI()
app.include_router(menu_router, prefix='/api/v1/menus')
app.include_router(submenu_router, prefix='/api/v1/menus')
app.include_router(dish_router, prefix='/api/v1/menus')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1")
    