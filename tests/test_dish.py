import uuid

import pytest


class TestDishes:
    @pytest.fixture(scope='class', autouse=True)
    def make_menu(self, client):
        response = client.post(
            "/api/v1/menus",
            json={"title": "My menu 1",
                  "description": "My menu description 1"}
        )
        global MENU_ID
        MENU_ID = response.json()["id"]

    @pytest.fixture(scope='class', autouse=True)
    def make_submenu(self, client):
        response = client.post(
            f"/api/v1/menus/{MENU_ID}/submenus",
            json={"title": "My submenu 1",
                  "description": "My submenu description 1"}
        )
        global SUBMENU_ID
        SUBMENU_ID = response.json()["id"]

    def test_create_dish(self, client):
        response = client.post(
            f"/api/v1/menus/{MENU_ID}/submenus/{SUBMENU_ID}/dishes",
            json={
                "title": "My dish 1",
                "description": "My dish description 1",
                "price": "12.50"
            }
        )
        global DISH_ID
        DISH_ID = response.json()["id"]
        assert response.status_code == 201
        assert response.json() == {
            "id": DISH_ID,
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": "12.50",
            "menu_id": MENU_ID,
            "submenu_id": SUBMENU_ID
        }

    def test_get_count_dishes(self, client):
        response = client.get(f"/api/v1/menus/{MENU_ID}"
                              f"/submenus/{SUBMENU_ID}/dishes")
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_check_dish_1(self, client):
        response = client.get(
            f"/api/v1/menus/{MENU_ID}"
            f"/submenus/{SUBMENU_ID}/dishes/{DISH_ID}")
        assert response.status_code == 200
        assert response.json() == {
            "id": DISH_ID,
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": "12.50",
            "menu_id": MENU_ID,
            "submenu_id": SUBMENU_ID
        }

    def test_check_fake_dish(self, client):
        fake_dish_id = uuid.uuid4()
        response = client.get(
            f"/api/v1/menus/{MENU_ID}"
            f"/submenus/{SUBMENU_ID}/dishes/{fake_dish_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Dish is not found."}

    def test_update_dish(self, client):
        response = client.patch(
            f"/api/v1/menus/{MENU_ID}"
            f"/submenus/{SUBMENU_ID}/dishes/{DISH_ID}",
            json={
                "title": "Updated dish 1",
                "description": "Updated dish description 1",
                "price": "1122.55"
            }
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": DISH_ID,
            "title": "Updated dish 1",
            "description": "Updated dish description 1",
            "price": "1122.55",
            "menu_id": MENU_ID,
            "submenu_id": SUBMENU_ID
        }

    def test_check_dish_2(self, client):
        response = client.get(
            f"/api/v1/menus/{MENU_ID}"
            f"/submenus/{SUBMENU_ID}/dishes/{DISH_ID}")
        assert response.status_code == 200
        assert response.json() == {
            "id": DISH_ID,
            "title": "Updated dish 1",
            "description": "Updated dish description 1",
            "price": "1122.55",
            "menu_id": MENU_ID,
            "submenu_id": SUBMENU_ID
        }

    def test_delete_dish(self, client):
        response = client.delete(f"/api/v1/menus/{MENU_ID}"
                                 f"/submenus/{SUBMENU_ID}"
                                 f"/dishes/{DISH_ID}")
        assert response.status_code == 200
        assert response.json() == {'detail': 'Dish is deleted successfully.'}

    def test_check_dish_3(self, client):
        response = client.get(f"/api/v1/menus/{MENU_ID}"
                              f"/submenus/{SUBMENU_ID}"
                              f"/dishes/{DISH_ID}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Dish is not found."}

    def test_get_dishes(self, client):
        response = client.get(f"/api/v1/menus/{MENU_ID}"
                              f"/submenus/{SUBMENU_ID}/dishes")
        assert response.status_code == 200
        assert response.json() == []
