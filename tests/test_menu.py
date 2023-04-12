import uuid


class TestMenus:
    def test_create_menu(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        assert menu.status_code == 201
        assert menu.json() == {
            "id": menu_id,
            "title": "My menu 1",
            "description": "My menu description 1",
            "submenus_count": 0,
            "dishes_count": 0
        }

    def test_get_count_menus(self, client):
        response = client.get("/api/v1/menus")
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_check_menu_1(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        response = client.get(f"/api/v1/menus/{menu_id}")
        assert response.status_code == 200
        assert response.json() == {
            "id": menu_id,
            "title": "My menu 1",
            "description": "My menu description 1",
            "submenus_count": 0,
            "dishes_count": 0
        }

    def test_check_fake_dish(self, client):
        fake_dish_id = uuid.uuid4()
        response = client.get(
            f"/api/v1/menus/{fake_dish_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Menu is not found."}

    def test_update_menu(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        response = client.patch(
            f"/api/v1/menus/{menu_id}",
            json={"title": "Updated title 1",
                  "description": "Updated description 1"}
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": menu_id,
            "title": "Updated title 1",
            "description": "Updated description 1",
            "submenus_count": 0,
            "dishes_count": 0
        }

    def test_check_menu_2(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        response = client.get(f"/api/v1/menus/{menu_id}")
        assert response.status_code == 200
        assert response.json() == {
            "id": menu_id,
            "title": "Updated title 1",
            "description": "Updated description 1",
            "submenus_count": 0,
            "dishes_count": 0
        }

    def test_delete_menu(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        response = client.delete(f"/api/v1/menus/{menu_id}")
        assert response.status_code == 200
        assert response.json() == {'detail': 'Menu is deleted successfully.'}

    def test_check_menu_3(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        response = client.get(f"/api/v1/menus/{menu_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Menu is not found."}

    def test_get_menus(self, client):
        """Returns an empty list"""
        response = client.get("/api/v1/menus")
        assert response.status_code == 200
        assert response.json() == []
