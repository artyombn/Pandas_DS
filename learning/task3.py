"""
Сколько в среднем в течение дня разговаривают по телефону нелояльные пользователи?
Нелояльные пользователи - Churn=1
Используйте показатель Total day minutes
"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    'https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/telecom_churn.csv',
    sep=','
)

print(df[df["Churn"] == True][["Total day minutes"]].mean())