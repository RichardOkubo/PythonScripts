import skfuzzy as fuzz
from numpy import arange
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(arange(0, 120), "temperatura")
porcentagem_de_nuvens = ctrl.Antecedent(arange(0, 110), "porcentagem_de_nuvens")
velocidade = ctrl.Consequent(arange(0, 150), "velocidade")

temperatura["freezing"] = fuzz.trapmf(temperatura.universe, [0, 0, 30, 50])
temperatura["cool"] = fuzz.trimf(temperatura.universe, [30, 50, 70])
temperatura["warm"] = fuzz.trimf(temperatura.universe, [50, 70, 90])
temperatura["hot"] = fuzz.trapmf(temperatura.universe, [70, 90, 120, 120])

porcentagem_de_nuvens["sunny"] = fuzz.trapmf(
    porcentagem_de_nuvens.universe, [0, 0, 20, 40]
)
porcentagem_de_nuvens["partly_cloudy"] = fuzz.trimf(
    porcentagem_de_nuvens.universe, [20, 50, 80]
)
porcentagem_de_nuvens["overcast"] = fuzz.trapmf(
    porcentagem_de_nuvens.universe, [60, 80, 110, 110]
)

velocidade["slow"] = fuzz.trapmf(velocidade.universe, [0, 0, 25, 75])
velocidade["fast"] = fuzz.trapmf(velocidade.universe, [25, 75, 150, 150])

regra_1 = ctrl.Rule(
    porcentagem_de_nuvens["sunny"] & temperatura["warm"], velocidade["fast"]
)
regra_2 = ctrl.Rule(
    porcentagem_de_nuvens["partly_cloudy"] & temperatura["cool"], velocidade["slow"]
)

velocidade_ctrl = ctrl.ControlSystem([regra_1, regra_2])
velocidade_simulador = ctrl.ControlSystemSimulation(velocidade_ctrl)


# Testando
velocidade_simulador.input["temperatura"] = 65  # em F°
velocidade_simulador.input["porcentagem_de_nuvens"] = 25  # 25%

velocidade_simulador.compute()
print(velocidade_simulador.output["velocidade"])

# temperatura.view(sim=velocidade_simulador)
# porcentagem_de_nuvens.view(sim=velocidade_simulador)
# velocidade.view(sim=velocidade_simulador)
