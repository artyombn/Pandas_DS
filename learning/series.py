"""
Создание Series
"""

import pandas as pd
import numpy as np

data = np.array(['a', 'b', 'c', 'd'])
# print(data)
# print(type(data))

s = pd.Series(data)
# print(s)
# print(type(s))

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
# print(s)

data = (1, 2, 3, 4)
indexes = ['a','b','a','d']
s = pd.Series(data, index=indexes) # data = pd.Series((1, 2, 3, 4), index=['a','b','a','d'])
print(s)
print(f"------")
print(s["a"])
print(s["d"])
print(s.iloc[0])
print(s.iloc[3])

print(s[["b", "d"]])
print(f"------")
print(s[2:]) # срез по позиции (считая от начала)
print(s[-2:]) # срез с конца (всегда работает)
