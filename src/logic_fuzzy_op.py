import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl

x = ctrl.Antecedent(np.arange(0.0, 2.0), "X")
y = ctrl.Consequent(np.arange(0.0, 2), "Y")

x.automf(names=["pequeno", "médio", "grande"])
y.automf(names=["baixo", "alto"])

regra_1 = ctrl.Rule(antecedent=x["pequeno"], consequent=y["baixo"], label="regra_1")
regra_2 = ctrl.Rule(antecedent=x["médio"], consequent=y["baixo"], label="regra_2")
regra_3 = ctrl.Rule(antecedent=x["médio"], consequent=y["alto"], label="regra_3")  ####
regra_4 = ctrl.Rule(antecedent=x["grande"], consequent=y["alto"], label="regra_4")  ####


controlador = ctrl.ControlSystem(rules=[regra_1, regra_2, regra_3, regra_4])
simulador = ctrl.ControlSystemSimulation(control_system=controlador)

# -----------------------------------------------------------------------------


def gerador(n=50):
    amostras = []
    for amostra in range(n):
        x = np.random.random()
        y = x ** 2
        amostras.append([x, y])
    return amostras


def main(amostras, valores, verboso=False):
    soma_dos_erros = 0

    for i, amostra in enumerate(amostras.values):
        print("---------------------") if verboso else None
        simulador.input["X"] = amostra
        simulador.compute()
        if verboso:
            print(f"AMOSTRA {i}\nX={amostra:.4f}\nY={simulador.output['Y']:.4f}\n")

        soma_dos_erros += (valores[i] - amostra) ** 2
    erro_total = soma_dos_erros / len(amostras)
    print("---------------------") if verboso else None
    print(f"ERRO TOTAL: {erro_total:.4f}")

    # x.view(sim=simulador)
    # y.view(sim=simulador)


if __name__ == "__main__":

    # df = pd.read_csv('dados.csv', header=None)
    df = pd.DataFrame(gerador(50))

    A = df[0]
    B = df[1]

    main(A, B)

    input()
