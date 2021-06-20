import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

link = "arquivo.csv"

df = pd.read_csv(link)
df["data"] = pd.to_datetime(df["data"])
df.set_index("data", inplace=True)

# df['valor'].diff().plot(); plt.show()

arima = ARIMA(df["valor"], freq="MS", order=(3, 1, 3)).fit()

# print((arima.resid ** 2).mean())
print(arima.forecast())  # previsão do próximo período

# plt.plot(df['valor']); plt.plot(arima.predict(typ='levels')); plt.show()
