import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

dados = {
    'Medicamento': [
        'I', 'I', 'I', 'I',
        'II', 'II', 'II', 'II', 'II',
        'III', 'III', 'III', 'III'],
    'Y': [  # Tempo de duração para o remédio surtir efeito
        12, 15, 17, 12,
        16, 14, 21, 15, 19,
        14, 17, 20, 15
    ]
}

df = pd.DataFrame(data=dados)

modelo = ols("Y ~ C(Medicamento)", data=df).fit()
# modelo.summary()

tabela_anova = anova_lm(modelo, typ=2)

print(tabela_anova)

p_valor = tabela_anova["PR(>F)"]["C(Medicamento)"]

alfa = 0.05

if p_valor < alfa:  # Rejeita H-zero
    print(
        "Há evidência suficiente, ao nível de significância de 5%, para concluir que há diferença na duração média de tempo que os três analgésicos levam para proporcionar alívio para dores de cabeça."
    )
else:  # Não rejeita H-zero
    print(
        "Não há evidência suficiente, ao nível de significância de 5%, para concluir que há diferença na duração média de tempo que os três analgésicos levam para proporcionar alívio para dores de cabeça."
    )
