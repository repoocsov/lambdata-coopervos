# my_lambdata/pizza.py


class Pizza:
    """
    Pizza object
    """

    def __init__(self, toppings, store, price):
        self._toppings = toppings
        self._store = store
        self._price = price

    @property
    def toppings(self):
        x = ""
        for topping in self._toppings:
            x += topping + ", "

        return print('YESSSSSSSS', x, "PIZZZZZZA")
