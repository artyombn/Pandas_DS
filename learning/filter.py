"""
Фильтрация
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)

print((df['Total eve minutes'] < 200)[:5])
print(df[(df['Total eve minutes'] < 200) & (df.State.isin(['NY', 'IN']))])
print(df[(df['Total day minutes'] > df['Total day minutes'].mean()) & (df['International plan'] == 'No')])
