import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

link = "arquivo.csv"

df = pd.read_csv(link)
df["data"] = pd.to_datetime(df["data"])
df.set_index("data", inplace=True)

sarima = SARIMAX(
    df["valor"], freq="MS", order=(3, 1, 3), seasonal_order=(3, 1, 2, 12)
).fit()

erro = (sarima.resid ** 2).mean()
print(erro)
