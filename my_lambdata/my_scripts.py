# FILENAME HERE


import pandas as pd
from my_lambdata.my_mod import enlarge


df = pd.DataFrame({"State": ['MI', 'WI']})
print(df.head())

x = 5
print("Number:", x)
print("Enlarged number:", enlarge(x))