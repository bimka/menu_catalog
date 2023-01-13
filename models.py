class Menu():

    counter = 0

    def __init__(self, name):
        self.name = name
        Menu.counter += 1



class Submenu(Menu):

    counter = 0

    def __init__(self, name):
        self.name = name
        Submenu.counter += 1



class Food(Submenu):

    counter = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Food.counter += 1

    def get_price(self):
        rounded_price = round(self.price, 2)
        return rounded_price

a = Submenu('one')
b = Menu('two')
c = Submenu('three')
d = Food('four', 30.126)

print(d.get_price())