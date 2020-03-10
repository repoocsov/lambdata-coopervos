# my_lambdata/pizza.py
from .food import Food

class Pizza(Food):
    """
    Pizza object
    Inherits from Food
    """

    def __init__(self):
        super().__init__()

        toppings = ['cheese']
        response = 1
        while response == 1:
            topping = input("What topping would you like to add to your pizza?")
            toppings.append(topping)
            response = int(input("Add another topping?\n0) No\n1) Yes"))

        self._toppings = toppings
        self._price = 5.88 + (2.00 * len(toppings))
        

    @property
    def message(self):
        x = ""
        for topping in self._toppings:
            # if (~topping == self._toppings[-1]):
            #     x += topping + ", "
            # else:
            #     x += topping + " "
            x += topping + ", "

        return print('The toppings for this pizza are ', x, '\n\n', 'This pizza is from', super().store,
        " and it's", super().taste, "\n\nPrice:", self._price)
