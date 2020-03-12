# my_lambdata/food.py

class Food:
    """
    Food object
    """

    def __init__(self):
        if __name__ == '__main__':
            store = input("Where are you getting this pizza from?")
        else:
            store = "Pizza Hut"
        taste = "Delicious"
        self._store = store
        self._taste = taste

    @property
    def store(self):
        return self._store

    @property
    def taste(self):
        return self._taste
