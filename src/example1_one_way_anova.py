"""
DESCRIÇÃO DO PROBLEMA

	Um pesquisador acredita que os salários médios dos atores, atletas e músicos mais bem pagos são os mesmos. Suponha que as
populações são normalmente distribuídas, as amostras são independentes e as variâncias populacionais são iguais. Para 'alfa de 10%',
você pode rejeitar a afirmação de que os salários médios são os mesmos para as três categorias?

Ho: as médias populacionais são similares (afirmação)
Ha: as médias populacionais diferem entre si
"""

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

dados = {
    "x": [
        "ator", "ator", "ator", "ator", "ator", "ator", "ator", "ator", "ator",
        "ator", "ator", "ator", "ator", "ator", "atleta", "atleta", "atleta",
        "atleta", "atleta", "atleta", "atleta", "atleta", "atleta", "atleta",
        "músico", "músico", "músico", "músico", "músico", "músico", "músico",
        "músico", "músico", "músico", "músico", "músico", "músico", "músico",
        "músico",
    ],
    "y": [
        75, 37, 37, 36, 33, 30, 30, 27, 26, 25, 25, 20, 11, 9, 67, 58, 53, 52,
        50, 46, 33, 26, 18, 13, 80, 60, 58, 57, 55, 45, 45, 44, 40, 38, 35, 35,
        32, 23, 15,
    ],
}

df = pd.DataFrame(data=dados)

modelo = ols("y ~ C(x)", data=df).fit()

tabela = anova_lm(modelo, typ=2)

print(tabela)

p_valor = tabela["PR(>F)"]["C(x)"]

alfa = 0.10

if p_valor < alfa:  # Rejeita H-zero
    print(
        """\nHá evidência suficiente, ao nível de significância de 10%, para rejeitar a afirmação de que os salários médios são os mesmos."""
    )
else:  # Não rejeita H-zero
    print(
        """\nNão há evidência suficiente, ao nível de significância de 10%, para rejeitar a afirmação de que os salários médios são os mesmos."""
    )
input()
