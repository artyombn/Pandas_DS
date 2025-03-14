"""
Группировка и агрегация
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)

columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df1 = df.groupby(['Churn'])[columns_to_show].sum()
print(df1)
print(df1.reset_index())
print(f"----------------")

columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']
df2 = df.groupby(['Churn'])[columns_to_show].agg(['mean', 'max', 'std', 'min'])
print(df2)
print(f"----------------")

df3 = pd.crosstab(df['Churn'], df['International plan'])
print(df3)
print(f"----------------")

df4 = df.pivot_table(
    values=['Total day calls', 'Total eve calls', 'Total night calls'],
    index=['Area code'],
    aggfunc='count',
    margins=True,
)
print(df4)