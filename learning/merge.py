"""
Слияние данных. Concat, Join, Merge
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    {
        'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
        'data1': range(7)
    }
)
df2 = pd.DataFrame(
    {
        'key': ['a', 'b', 'd'],
        'data2': range(3)
    }
)

print(df1)
print(df2)
print(f"-----------")

merge1 = pd.merge(df1, df2)
print(merge1)
print(f"-----------")

merge_left = pd.merge(df1, df2, how='left')
print(merge_left)
print(f"-----------")

merge_right = pd.merge(df1, df2, how='right')
print(merge_right)
print(f"-----------")

merge_outer = pd.merge(df1, df2, how='outer')
print(merge_outer)
print(f"-----------")

df3 = pd.DataFrame(
    {
        'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
        'data1': range(7)
    }
)

df4 = pd.DataFrame(
    {
        'rkey': ['a', 'b', 'd'],
        'data2': range(3)
    }
)

print(df3)
print(df4)
print(f"-----------")

merge_by_columns = pd.merge(df3, df4, left_on='lkey', right_on='rkey')
print(merge_by_columns)

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

print(left)
print(right)
print(f"-----------")

add_left_right = pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
print(add_left_right)


df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                  'data2': range(3)})

print(f"-----------")
print(df1)
print(df2)
print(f"-----------")
print(pd.concat([df1,df2]))
print(f"-----------")
print(pd.concat([df1,df2],axis=1))
print(f"-----------")