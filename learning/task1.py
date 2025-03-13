"""
Возьмите последние две строки и два столбца из предыдущего датафрейма методом iloc.
Удалите из среза произвольный столбик
"""
import pandas as pd
import numpy as np

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10,20,30], index=['a','b','c']),
     }
df = pd.DataFrame(d)
print(df)

print(df.iloc[-2:, -2:].drop('two', axis=1))