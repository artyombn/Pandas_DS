"""
Статистика
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)

print(df.iloc[985])
print(df['Total intl calls'].median())
print(df['Total intl calls'].mean())
print(df['Total intl calls'].std())
print(f"-------------------")
print(df.describe())
print(f"-------------------")
print(df.describe(include=['object', 'bool']))
print(f"-------------------")
print(df['State'].value_counts())
print(df['State'].unique())
print(f"-------------------")
print(df['Voice mail plan'].value_counts(normalize=True))
print(f"-------------------")
print(df.sort_values(by='Total day charge', ascending=False).head())
print(df.sort_values(by='Total day charge', ascending=False)[['Total day charge']].head())

print(f"-------------------")
print(df.sort_values(by=['Area code', 'Total day charge'], ascending=[True, False])[['Total day charge']].head())


if __name__ == "__main__":
    df['Area code'].value_counts(normalize=True).plot.barh()
    # plt.show()