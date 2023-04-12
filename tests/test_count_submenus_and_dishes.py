import pytest


class TestCountSubmenusAndDishes:
    def test_count_in_menu_1(self, client, make_menu):
        menu_id = make_menu
        response = client.get(f"/api/v1/menus/{menu_id}")
        print(response.json())
        assert response.json()["dishes_count"] == 3
        assert response.json()["submenus_count"] == 1

    def test_count_in_menu_2(self, client, make_menu,
                             make_submenu, make_dish_2):
        menu_id = make_menu
        submenu_id = make_submenu
        dish_id = make_dish_2
        client.delete(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}"
                      f"/dishes/{dish_id}")
        response = client.get(f"/api/v1/menus/{menu_id}")
        assert response.json()["dishes_count"] == 2
        assert response.json()["submenus_count"] == 1

    def test_count_in_menu_3(self, client, make_menu,
                             make_submenu):
        menu_id = make_menu
        submenu_id = make_submenu
        client.delete(f"/api/v1/menus/{menu_id}/submenus/{submenu_id}")
        response = client.get(f"/api/v1/menus/{menu_id}")
        assert response.json()["dishes_count"] == 0
        assert response.json()["submenus_count"] == 0

