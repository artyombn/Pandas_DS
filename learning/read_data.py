"""
Загрузка данных
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=',',
)

print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

print(df.shape)
print(df.columns)
print(df.index)

chunker = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    chunksize=1000,
)

z = 0
for chunk in chunker:
    print(chunk.shape)
    # print(chunk.head()) # покажет первые 5 строк чанка
    # print(chunk) # Выведет весь чанк


df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)
# df.to_excel('test.xlsx')
# df.to_excel('test1.xlsx', index=False, header=False)
# df.head()
print(f"------------1")
# print(df)
# pd.set_option('display.max_columns', 20)
# pd.set_option('display.max_rows', 20)
# print(df.info())
print(f"------------2")
print(len(df.columns))
# print(df.isna().sum())
print(f"------------3")

df = pd.DataFrame([[1, None, 2],
                   [2, 3, 5],
                   [np.nan, 4, 6],
                   ], index=['a', 'b', 'c'])
print(df)
# print(df.isna().sum())
# print(df[df.isna().any(axis=1)])
print(df.isna())
print(df.dropna(how='all'))
print(df.fillna(999))

print(f"---------------")
d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10,20,30], index=['a', 'b', 'c']),
     }
df = pd.DataFrame(d)
print(df)
print(df.ffill())

print(f"---------------")
df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)
print(df.head())
print(df.dtypes)
print(df['Churn'].value_counts())
print(f"---------")
print(df.Churn.dtypes)