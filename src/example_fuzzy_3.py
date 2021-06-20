import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

## Criando as variáveis do problema

# Antecedentes
design = ctrl.Antecedent(np.arange(1, 6), "design")
potencia = ctrl.Antecedent(np.arange(1, 6), "potencia")
economia = ctrl.Antecedent(np.arange(1, 6), "economia")
preco = ctrl.Antecedent(np.arange(1, 6), "preco")
espaco = ctrl.Antecedent(np.arange(1, 6), "espaco")

# Consequente
percepcao = ctrl.Consequent(np.arange(1, 6), "percepcao")


## Criando os atributos

# Design
design["feio"] = fuzz.trapmf(design.universe, [1, 1, 2, 3])
design["razoável"] = fuzz.trapmf(design.universe, [2, 3, 3, 4])
design["belo"] = fuzz.trapmf(design.universe, [3, 4, 5, 5])

# Potência
potencia["baixa"] = fuzz.trapmf(potencia.universe, [1, 1, 2, 3])
potencia["média"] = fuzz.trapmf(potencia.universe, [2, 3, 3, 4])
potencia["alta"] = fuzz.trapmf(potencia.universe, [3, 4, 5, 5])

# Economia
economia["baixa"] = fuzz.trapmf(economia.universe, [1, 1, 2, 3])
economia["média"] = fuzz.trapmf(economia.universe, [2, 3, 3, 4])
economia["alta"] = fuzz.trapmf(economia.universe, [3, 4, 5, 5])

# Preço
preco["elevado"] = fuzz.trapmf(preco.universe, [1, 1, 2, 3])
preco["coerente"] = fuzz.trapmf(preco.universe, [2, 3, 3, 4])
preco["barato"] = fuzz.trapmf(preco.universe, [3, 4, 5, 5])

# Espaço Interno
espaco["apertado"] = fuzz.trapmf(espaco.universe, [1, 1, 2, 3])
espaco["médio"] = fuzz.trapmf(espaco.universe, [2, 3, 3, 4])
espaco["espaçoso"] = fuzz.trapmf(espaco.universe, [3, 4, 5, 5])

# Percepção
percepcao["dispensável"] = fuzz.trapmf(percepcao.universe, [1, 1, 2, 3])
percepcao["importante"] = fuzz.trapmf(percepcao.universe, [2, 3, 3, 4])
percepcao["crucial"] = fuzz.trapmf(percepcao.universe, [3, 4, 5, 5])


## Regras

# Regra (só para teste)
regra = ctrl.Rule(
    antecedent=(
        design["feio"]
        | potencia["baixa"]
        | economia["baixa"]
        | preco["elevado"]
        | espaco["apertado"]
    ),
    consequent=percepcao["dispensável"],
    label="regra",
)

percepcao_ctrl = ctrl.ControlSystem(regra)
percepcao_simulador = ctrl.ControlSystemSimulation(percepcao_ctrl)

###############################################################################

## Exemplo de regras complexas

# rule0 = ctrl.Rule(
#     antecedent=(
#         (error["nb"] & delta["nb"])
#         | (error["ns"] & delta["nb"])
#         | (error["nb"] & delta["ns"])
#     ),
#     consequent=output["nb"],
#     label="rule nb",
# )
#
# rule1 = ctrl.Rule(
#     antecedent=(
#         (error["nb"] & delta["ze"])
#         | (error["nb"] & delta["ps"])
#         | (error["ns"] & delta["ns"])
#         | (error["ns"] & delta["ze"])
#         | (error["ze"] & delta["ns"])
#         | (error["ze"] & delta["nb"])
#         | (error["ps"] & delta["nb"])
#     ),
#     consequent=output["ns"],
#     label="rule ns",
# )
#
# rule2 = ctrl.Rule(
#     antecedent=(
#         (error["nb"] & delta["pb"])
#         | (error["ns"] & delta["ps"])
#         | (error["ze"] & delta["ze"])
#         | (error["ps"] & delta["ns"])
#         | (error["pb"] & delta["nb"])
#     ),
#     consequent=output["ze"],
#     label="rule ze",
# )
#
# rule3 = ctrl.Rule(
#     antecedent=(
#         (error["ns"] & delta["pb"])
#         | (error["ze"] & delta["pb"])
#         | (error["ze"] & delta["ps"])
#         | (error["ps"] & delta["ps"])
#         | (error["ps"] & delta["ze"])
#         | (error["pb"] & delta["ze"])
#         | (error["pb"] & delta["ns"])
#     ),
#     consequent=output["ps"],
#     label="rule ps",
# )
#
# rule4 = ctrl.Rule(
#     antecedent=(
#         (error["ps"] & delta["pb"])
#         | (error["pb"] & delta["pb"])
#         | (error["pb"] & delta["ps"])
#     ),
#     consequent=output["pb"],
#     label="rule pb",
# )

###############################################################################

## Testando


def modelo(atributos, view_on=False):
    # Entradas
    percepcao_simulador.input["design"] = atributos[0]
    percepcao_simulador.input["potencia"] = atributos[1]
    percepcao_simulador.input["economia"] = atributos[2]
    percepcao_simulador.input["preco"] = atributos[3]
    percepcao_simulador.input["espaco"] = atributos[4]

    # Saída
    percepcao_simulador.compute()

    # View
    if view_on:
        percepcao.view(sim=percepcao_simulador)

    return percepcao_simulador.output["percepcao"]


# modelo([1, 2, 3, 4, 5]))

A = [
    [1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2],
    [1, 3, 3, 3, 3],
    [1, 4, 4, 4, 4],
    [1, 5, 5, 5, 5],
]

df = pd.DataFrame(A)
df["modelo"] = df.apply(modelo, axis=1)
print(df)


## Outro assunto

# B = [[1, 2, 3],
#     [4, 5, 6]]
# np.concatenate([A for i in range(3)])
