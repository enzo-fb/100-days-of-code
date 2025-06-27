"""Pandas"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
dados2 = {
    "frutas": ["maçã", "banana", "laranja", "uva"],
    "preços": [1.2, 0.5, 0.8, 1.5],
}

df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(dados2)
print(df2[0:2])
