"""
Подготовка данных
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)

# print(df.apply(np.max))

mean_value = df['Total intl calls'].mean()
print(mean_value)

def checker(variable):
    if variable <= mean_value:
        return 'Мало звонков'
    else:
        return 'Много звонков'

print(checker(5))

df['Calls'] = df['Total intl calls'].apply(checker)
print(df.Calls)

d = {"No": False, "Yes": True}
df['International plan'] = df['International plan'].map(d)
print(df["International plan"])

df = df.replace({'Voice mail plan': d})
print(df["Voice mail plan"])