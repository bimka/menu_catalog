import uuid


class TestSubmenus:
    def test_create_submenu(self, client, make_submenu):
        submenu = make_submenu
        submenu_id = submenu.json()["id"]
        assert submenu.status_code == 201
        assert submenu.json() == {
            "id": submenu_id,
            "title": "My submenu 1",
            "description": "My submenu description 1",
            "dishes_count": 0
        }

    # def test_get_count_submenus(self, client, make_menu):
    #     menu = make_menu
    #     menu_id = menu.json()["id"]
    #     response = client.get(f"/api/v1/menus/{menu_id}/submenus")
    #     assert response.status_code == 200
    #     assert len(response.json()) == 1

    def test_check_submenu_1(self, client, make_menu, make_submenu):
        menu = make_menu
        menu_id = menu.json()["id"]
        submenu = make_submenu
        submenu_id = submenu.json()["id"]
        response = client.get(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}")
        assert response.status_code == 200
        assert response.json() == {
            "id": submenu_id,
            "title": "My submenu 1",
            "description": "My submenu description 1",
            "dishes_count": 0
        }

    def test_check_fake_submenu(self, client, make_menu):
        menu = make_menu
        menu_id = menu.json()["id"]
        fake_submenu_id = uuid.uuid4()
        response = client.get(
            f"/api/v1/menus/{menu_id}/submenus/{fake_submenu_id}"
        )
        assert response.status_code == 404
        assert response.json() == {"detail": "Submenu is not found."}

    def test_update_submenu(self, client, make_menu, make_submenu):
        menu = make_menu
        menu_id = menu.json()["id"]
        submenu = make_submenu
        submenu_id = submenu.json()["id"]
        response = client.patch(
            f"/api/v1/menus/{menu_id}/submenus/{submenu_id}",
            json={
                "title": "Updated submenu 1",
                "description": "Updated submenu description 1"
            }
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": submenu_id,
            "title": "Updated submenu 1",
            "description": "Updated submenu description 1",
            "dishes_count": 0
        }

    def test_check_submenu_2(self, client, make_menu, make_submenu):
        menu = make_menu
        menu_id = menu.json()["id"]
        submenu = make_submenu
        submenu_id = submenu.json()["id"]
        response = client.get(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}")
        assert response.status_code == 200
        assert response.json() == {
            "id": submenu_id,
            "title": "Updated submenu 1",
            "description": "Updated submenu description 1",
            "dishes_count": 0
        }

    def test_delete_submenu(self, client, make_menu, make_submenu):
        menu = make_menu
        menu_id = menu.json()["id"]
        submenu = make_submenu
        submenu_id = submenu.json()["id"]
        response = client.delete(f"/api/v1/menus/{menu_id}"
                                 f"/submenus/{submenu_id}")
        assert response.status_code == 200
        assert response.json() == {'detail': 'Submenu is deleted successfully.'}


    def test_check_submenu_3(self, client, make_menu, make_submenu):
        menu = make_menu
        menu_id = menu.json()["id"]
        submenu = make_submenu
        submenu_id = submenu.json()["id"]
        response = client.get(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}")
        assert response.status_code == 404
        assert response.json() == {"detail": "Submenu is not found."}

    # def test_get_submenus(self, client, make_menu):
    #     menu = make_menu
    #     menu_id = menu.json()["id"]
    #     response = client.get(f"/api/v1/menus/{menu_id}/submenus")
    #     assert response.status_code == 200
    #     assert response.json() == []