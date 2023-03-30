import uvicorn
from fastapi import FastAPI

from src.menus.router import menu_router
from src.submenus.router import submenu_router

app = FastAPI()
app.include_router(menu_router, prefix='/api/v1/menus')
app.include_router(submenu_router, prefix='/api/v1/menus/{menu_id}/submenus')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)