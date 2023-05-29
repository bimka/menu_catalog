import uuid


class TestDishes:
    def test_create_dish(self, client, make_menu, make_submenu, make_dish_1):
        menu = make_menu
        submenu = make_submenu
        dish = make_dish_1
        menu_id = menu.json()["id"]
        submenu_id = submenu.json()["id"]
        dish_id = dish.json()["id"]
        assert dish.status_code == 201
        assert dish.json() == {
            "id": dish_id,
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": "11.22",
            "menu_id": menu_id,
            "submenu_id": submenu_id,
        }

    # def test_get_count_dishes(self, client, make_menu, make_submenu):
    #     menu = make_menu
    #     submenu = make_submenu
    #     menu_id = menu.json()["id"]
    #     submenu_id = submenu.json()["id"]
    #     response = client.get(f"/api/v1/menus/{menu_id}"
    #                           f"/submenus/{submenu_id}/dishes")
    #     assert response.status_code == 200
    #     assert len(response.json()) == 1

    def test_check_dish_1(self, client, make_menu, make_submenu, make_dish_1):
        menu = make_menu
        submenu = make_submenu
        dish = make_dish_1
        menu_id = menu.json()["id"]
        submenu_id = submenu.json()["id"]
        dish_id = dish.json()["id"]
        response = client.get(
            f"/api/v1/menus/{menu_id}"
            f"/submenus/{submenu_id}/dishes/{dish_id}"
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": dish_id,
            "title": "My dish 1",
            "description": "My dish description 1",
            "price": "11.22",
            "menu_id": menu_id,
            "submenu_id": submenu_id,
        }

    def test_check_fake_dish(self, client, make_menu, make_submenu):
        menu = make_menu
        submenu = make_submenu
        menu_id = menu.json()["id"]
        submenu_id = submenu.json()["id"]
        fake_dish_id = uuid.uuid4()
        response = client.get(
            f"/api/v1/menus/{menu_id}"
            f"/submenus/{submenu_id}/dishes/{fake_dish_id}"
        )
        assert response.status_code == 404
        assert response.json() == {"detail": "Dish is not found."}

    def test_update_dish(self, client, make_menu, make_submenu, make_dish_1):
        menu = make_menu
        submenu = make_submenu
        dish = make_dish_1
        menu_id = menu.json()["id"]
        submenu_id = submenu.json()["id"]
        dish_id = dish.json()["id"]
        response = client.patch(
            f"/api/v1/menus/{menu_id}"
            f"/submenus/{submenu_id}/dishes/{dish_id}",
            json={
                "title": "Updated dish 1",
                "description": "Updated dish description 1",
                "price": "1122.55",
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": dish_id,
            "title": "Updated dish 1",
            "description": "Updated dish description 1",
            "price": "1122.55",
            "menu_id": menu_id,
            "submenu_id": submenu_id,
        }

    # def test_check_dish_2(self, client,
    #                            make_menu,
    #                            make_submenu,
    #                            make_dish_1):
    #     menu = make_menu
    #     submenu = make_submenu
    #     dish = make_dish_1
    #     menu_id = menu.json()["id"]
    #     submenu_id = submenu.json()["id"]
    #     dish_id = dish.json()["id"]
    #     response = client.get(
    #         f"/api/v1/menus/{menu_id}"
    #         f"/submenus/{submenu_id}/dishes/{dish_id}")
    #     assert response.status_code == 200
    #     assert response.json() == {
    #         "id": dish_id,
    #         "title": "Updated dish 1",
    #         "description": "Updated dish description 1",
    #         "price": "1122.55",
    #         "menu_id": menu_id,
    #         "submenu_id": submenu_id
    #     }

    def test_delete_dish(self, client, make_menu, make_submenu, make_dish_1):
        menu = make_menu
        submenu = make_submenu
        dish = make_dish_1
        menu_id = menu.json()["id"]
        submenu_id = submenu.json()["id"]
        dish_id = dish.json()["id"]
        response = client.delete(
            f"/api/v1/menus/{menu_id}"
            f"/submenus/{submenu_id}"
            f"/dishes/{dish_id}"
        )
        assert response.status_code == 200
        assert response.json() == {"detail": "Dish is deleted successfully."}

    def test_check_dish_3(self, client, make_menu, make_submenu, make_dish_1):
        menu = make_menu
        submenu = make_submenu
        dish = make_dish_1
        menu_id = menu.json()["id"]
        submenu_id = submenu.json()["id"]
        dish_id = dish.json()["id"]
        response = client.get(
            f"/api/v1/menus/{menu_id}"
            f"/submenus/{submenu_id}"
            f"/dishes/{dish_id}"
        )
        assert response.status_code == 404
        assert response.json() == {"detail": "Dish is not found."}

    # def test_get_dishes(self, client, make_menu, make_submenu):
    #     menu = make_menu
    #     submenu = make_submenu
    #     menu_id = menu.json()["id"]
    #     submenu_id = submenu.json()["id"]
    #     response = client.get(f"/api/v1/menus/{menu_id}"
    #                           f"/submenus/{submenu_id}/dishes")
    #     assert response.status_code == 200
    #     assert response.json() == []
