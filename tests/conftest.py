import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.src.session import engine
from app.src.models import Base


@pytest.fixture(scope="class", autouse=True)
def test_db():
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="class")
def client():
    yield TestClient(app)


@pytest.fixture(scope="class")
def make_menu(client):
    response = client.post(
        "/api/v1/menus",
        json={"title": "My menu 1", "description": "My menu description 1"},
    )
    yield response


@pytest.fixture(scope="class")
def make_submenu(client, make_menu):
    menu_id = make_menu.json()["id"]
    response = client.post(
        f"/api/v1/menus/{menu_id}/submenus",
        json={
            "title": "My submenu 1",
            "description": "My submenu description 1",
        },
    )
    yield response


@pytest.fixture(scope="class")
def make_dish_1(client, make_menu, make_submenu):
    menu_id = make_menu.json()["id"]
    submenu_id = make_submenu.json()["id"]
    response = client.post(
        f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
        json={
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": "11.22",
        },
    )
    yield response


@pytest.fixture(scope="class")
def make_dish_2(client, make_menu, make_submenu):
    menu_id = make_menu.json()["id"]
    submenu_id = make_submenu.json()["id"]
    response = client.post(
        f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
        json={
            "title": "My dish 2",
            "description": "My dish description 2",
            "price": "22.33",
        },
    )
    yield response


@pytest.fixture(scope="class")
def make_dish_3(client, make_menu, make_submenu):
    menu_id = make_menu.json()["id"]
    submenu_id = make_submenu.json()["id"]
    response = client.post(
        f"/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes",
        json={
            "title": "My dish 3",
            "description": "My dish description 3",
            "price": "33.44",
        },
    )
    yield response
