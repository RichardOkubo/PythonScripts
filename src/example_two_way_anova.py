import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# import numpy as np

dados = {
	'x': [  # Marcas
        'A', 'A', 'A', 'A',
        'B', 'B', 'B', 'B',
        'C', 'C', 'C', 'C'
    ],
    'y': [  # Tratamentos
        'I', 'II', 'III', 'IV',
        'I', 'II', 'III', 'IV',
        'I', 'II', 'III', 'IV'
    ],
    'z': [
    	.97, .48, .48, .46,
    	.77, .14, .22, .25,
    	.67, .39, .57, .19
    ]
}

# dados['z'] = (dados['z'] - np.mean(dados['z'], axis=0)) / np.std(dados['z'], axis=0)

df = pd.DataFrame(data=dados)

modelo = ols("z ~ C(x) + C(y) + C(x):C(y)", data=df).fit()

tabela = anova_lm(modelo, typ=2)

print(tabela)
input()
