# tests/test_pizza.py

import unittest
from my_lambdata.pizza import Pizza


class TestPizza(unittest.TestCase):
    """
    Tests the Pizza class
    """

    def test_pizza(self):
        pizza = Pizza()

        # _price should be a float
        self.assertTrue(isinstance(pizza._price, float))

        # _toppings should be a list
        self.assertTrue(isinstance(pizza._toppings, list))

        # message should be a string
        self.assertTrue(isinstance(pizza.message, str))


if __name__ == '__main__':
    unittest.main()
