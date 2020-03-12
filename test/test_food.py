# test_food.py

import unittest
from my_lambdata.food import Food


class TestFood(unittest.TestCase):
    """
    Tests the Food class
    """

    def test_food(self):
        food = Food()

        # _price should be a float
        self.assertEqual(food._taste, "Delicious")

        # message should be a string
        self.assertTrue(isinstance(food._store, str))


if __name__ == '__main__':
    unittest.main()
