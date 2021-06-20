"""Avaliador de relação custo-benefício."""
import skfuzzy as fuzz
from numpy import arange
from skfuzzy import control as ctrl


def main():
    """Executa o simulador."""
    print("\n------------------------- SIMULADOR -------------------------\n")
    custo_max = round(
        float(
            input(
                """Qual é o custo máximo que você está
disposto a pagar?
::: R$"""
            )
        )
    )
    print()
    custo_ = float(
        input(
            f"""Em um intervalo de 0 a {round(custo_max)},
Qual é o custo?
::: R$"""
        )
    )
    print()
    beneficio_ = int(
        input(
            """Em uma escala de 1 a 5, como você avalia o
benefício esperado?
[ 1 ] baixo
[ 2 ] baixo-moderado
[ 3 ] moderado
[ 4 ] moderado-alto
[ 5 } alto
::: """
        )
    )
    print()
    while True:
        sim_nao = input(
            """Mostrar status do simulador? [s/n]
::: """
        ).lower()
        if sim_nao in "sn":
            status = True if sim_nao == "s" else False
            break
    print()
    print(
        custo_beneficio_(
            custo=custo_,
            beneficio=beneficio_,
            status_=status,
            modelo=lógica_fuzzy(max_=custo_max),
        )
    )
    print("\n---------------------- FIM DO PROGRAMA ----------------------\n")


def custo_beneficio_(
    custo: float = 50.0, beneficio: int = 3, status_=False, modelo: callable = None
) -> str:
    """Avalia o custo-benefício, dado as valores de entrada do usuário."""
    modelo.input["custo"] = custo
    modelo.input["benefício"] = beneficio

    modelo.compute()
    resultado = modelo.output["custo-benefício"]

    if resultado < (100 * 1 / 3):
        return f"""SUGESÃO: custo-benefício BAIXO;
logo, não aceite. {f"¨STATUS: {resultado:.1f}" if status_ else ""}"""
    elif resultado < (100 * 2 / 3):
        return f"""SUGESÃO: custo-benefício MODERADO;
logo, negocie. {f"STATUS: {resultado:.1f}" if status_ else ""}"""
    else:
        return f"""SUGESÃO: custo-benefício Alto;
logo, aceite. {f"STATUS: {resultado:.1f}" if status_ else ""}"""


def lógica_fuzzy(max_=101):
    custo = ctrl.Antecedent(universe=arange(max_ + 1), label="custo")
    beneficio = ctrl.Antecedent(universe=arange(1, 6), label="benefício")
    custo_beneficio = ctrl.Consequent(universe=arange(101), label="custo-benefício")

    custo.automf(names=["baixo", "moderado", "alto"])
    beneficio.automf(variable_type="quant", names=["baixo", "moderado", "alto"])
    custo_beneficio.automf(names=["baixo", "moderado", "alto"])

    # custo.view()
    # beneficio.view()
    # custo_beneficio.view()

    regra_1 = ctrl.Rule(
        antecedent=(custo["baixo"] & beneficio["alto"]),
        consequent=custo_beneficio["alto"],
        label="regra 1",
    )
    regra_2 = ctrl.Rule(
        antecedent=(custo["moderado"] & beneficio["alto"]),
        consequent=custo_beneficio["alto"],
        label="regra 2",
    )
    regra_3 = ctrl.Rule(
        antecedent=(custo["baixo"] & beneficio["moderado"]),
        consequent=custo_beneficio["alto"],
        label="regra 3",
    )
    regra_4 = ctrl.Rule(
        antecedent=(custo["baixo"] & beneficio["baixo"]),
        consequent=custo_beneficio["moderado"],
        label="regra 4",
    )
    regra_5 = ctrl.Rule(
        antecedent=(custo["moderado"] & beneficio["moderado"]),
        consequent=custo_beneficio["moderado"],
        label="regra 5",
    )
    regra_6 = ctrl.Rule(
        antecedent=(custo["alto"] & beneficio["alto"]),
        consequent=custo_beneficio["moderado"],
        label="regra 6",
    )
    regra_7 = ctrl.Rule(
        antecedent=(custo["alto"] & beneficio["moderado"]),
        consequent=custo_beneficio["baixo"],
        label="regra 7",
    )
    regra_8 = ctrl.Rule(
        antecedent=(custo["moderado"] & beneficio["baixo"]),
        consequent=custo_beneficio["baixo"],
        label="regra 8",
    )
    regra_9 = ctrl.Rule(
        antecedent=(custo["alto"] & beneficio["baixo"]),
        consequent=custo_beneficio["baixo"],
        label="regra 9",
    )

    sistema_de_controle = ctrl.ControlSystem(
        rules=[
            regra_1, regra_2, regra_3, regra_4, regra_5, regra_6, regra_7,
            regra_8, regra_9,
        ]
    )

    simulador = ctrl.ControlSystemSimulation(control_system=sistema_de_controle)

    # custo.view(sim=simulador)
    # beneficio.view(sim=simulador)
    # custo_beneficio.view(sim=simulador)

    return simulador


if __name__ == "__main__":
    main()
    input()
