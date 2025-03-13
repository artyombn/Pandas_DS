"""
Создание Dataframe
"""

import pandas as pd
import numpy as np

# ИЗ СПИСКА
data = [['Alex', 'Semenov', 10], ['Bob', None, 12], ['Clarke', None, 13]]
df = pd.DataFrame(data, columns=['Name', 'Surname', 'Age'])
print(df)
print(type(df))

# ИЗ СЛОВАРЯ
data = {'Name': ['Alex', 'Ivan'], 'Age': [10, 12]}
df = pd.DataFrame(data)
print(df)

""""
Работа с Dataframe
"""

data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 32]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)
print(type(df))

print(df['Name'])
print(type(df['Name']))

# Создание Dataframe через Series
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     }

df = pd.DataFrame(d)
print(df)

print(df.loc['b'])

print(df['one'] > 1)
print(df.loc[df['one'] > 1])
print(df.loc[df['one'] > 1, ['two']])

print(df.iloc[-2:])

print(df.index)

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([3, 4, 6,11], index=['a', 'b', 'c', 'd']),
     'four': pd.Series([4, 8, 11,], index=['a', 'b', 'c']),
     }

df_series = pd.DataFrame(d)
print(df_series)

z = df_series.loc['b':'d', 'one':'three']
print(z)

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     }

df = pd.DataFrame(d)
print(f"Original DF: \n{df}")

df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(f"Updated DF: \n{df}")

df['four'] = df['one'] + df['two']
print(df)

del df['three']
print(df)

k = df.pop('two')
print(k)
print(df)

new_d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([3, 4, 6,11], index=['a', 'b', 'c', 'd']),
     'four': pd.Series([4, 8, 11,], index=['a', 'b', 'c']),
     }

df_series = pd.DataFrame(new_d)
print(f"Oroginal DF: \n{df_series}")

# axis= 1 -> удаляем по стобцам с указанием имени стобца
df_series = df_series.drop('two', axis=1)

# axis=0 -> удаляем по строкам с указанием марки индекса строки
df_series = df_series.drop('a', axis=0)
print(f"DF after drop: \n{df_series}")
