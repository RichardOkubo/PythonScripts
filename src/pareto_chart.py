import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.ticker import PercentFormatter

# Preparação dos dados
filename = "db.csv"
df = pd.read_csv(filename)
df = df.sort_values(by="Count",ascending=False)
df["Percent"] = df["Count"]/df["Count"].sum() * 100
df["CumPercent"] = df["Percent"].cumsum()

# Cria o barplot e define os dados os eixos, a cor das barras, titulo do gráfico
fig, ax = plt.subplots(figsize=(20,10))
ax.bar(df["Type"], df["Count"], color="C0")
ax.set_title("Pareto")

# Eixo secundário
ax2 = ax.twinx()

# Cria a Curva de Pareto no eixo secundário
ax2.plot(df["Type"], df["CumPercent"], color="C1", marker="D", ms=7, label='Pareto')
ax2.yaxis.set_major_formatter(PercentFormatter())

# Configurações dos eixos 
ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
ax2.set_ylim([0,110])

# Ajusta a inclinação dos labels do eixo x
for tick in ax.get_xticklabels():
    tick.set_rotation(45)

# Finalmente mostra o grafico definido acima
plt.legend() # para mostrar a legenda
plt.show()
