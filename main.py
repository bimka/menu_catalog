import uvicorn
from fastapi import FastAPI

from src.menus import router

app = FastAPI()
app.include_router(router.router, prefix='/api/v1/menus')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)