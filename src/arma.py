import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.arima_model import ARMA

link = "arquivo.csv"

df = pd.read_csv(link)
df["data"] = pd.to_datetime(df["data"])
df.set_index("data", inplace=True)

n = len(df["valor"])
train_size = int(n * 2 / 3)
train_set = df["valor"][:train_size]
test_set = df["valor"][train_size:]

arma33_train = ARMA(train_set, freq="MS", order=(3, 3)).fit()
arma33_test = ARMA(test_set, freq="MS", order=(3, 3)).fit(arma33_train.params)

arma = ARMA(df["valor"][:], freq="MS", order=(3, 3)).fit()

plt.figure(figsize=(10, 5))
plt.plot(train_set)
plt.plot(test_set)
plt.plot(arma33_test.predict())
plt.plot(arma.predict())
plt.plot(
    arma33_test.predict(start="2020-05-01", end="2020-05-01"), marker="x", color="red"
)
plt.plot(arma.predict(start="2020-05-01", end="2020-05-01"), marker="o", color="green")

print("*" * 20)
print(f"\nMédia do erro quadrático: {(arma33_test.resid ** 2).mean()}")
print(f"Média do erro quadrático: {(arma.resid ** 2).mean()}")

plt.show()
input()
