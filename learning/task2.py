"""
Верните параметр Churn к булевому формату данных
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)

print(df.head())
print(df.dtypes) # Churn bool
df.Churn = df.Churn.astype("bool")

# лучше использовать этот вариант, чтобы избежать конфликтов с именами столбцов, например такими как sum, mean
df['Churn'] = df['Churn'].astype('bool')