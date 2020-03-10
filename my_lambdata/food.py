class Food:
    """
    Food object
    """

    def __init__(self):
        store = input("Where are you getting this pizza from?")
        taste = "Delicious"
        self._store = store
        self._taste = taste

    @property
    def store(self):
        return self._store

    @property
    def taste(self):
        return self._taste