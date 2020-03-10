# my_lambdata/my_scripts.py

import pandas as pd
from my_lambdata.my_mod import enlarge
from my_lambdata.pizza import Pizza


topping1 = input("What is the first topping you would like for your pizza?")
topping2 = input("What is the SECOND topping you would like for your pizza?")
toppings = [topping1, topping2]

pizza = Pizza(toppings, "Pizza Hut", 7.99)

pizza.toppings