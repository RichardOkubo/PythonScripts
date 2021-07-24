"""Fuzzy logic algorithm applied to traditional expectation theory.

Source: https://www.ifm.eng.cam.ac.uk/research/dstools/vrooms-expectancy-theory/

Vroom's expectancy theory
    ...assumes that behavior results from conscious choices among
    alternatives whose purpose it is to maximize pleasure and minimize
    pain. Together with Edward Lawler and Lyman Porter, Victor Vroom
    suggested that the relationship between people's behavior at work
    and their goals was not as simple as was first imagined by other
    scientists. Vroom realized that an employee's performance is based
    on individuals factors such as personality, skills, knowledge,
    experience and abilities.

    The theory suggests that although individuals may have different
    sets of goals, they can be motivated if they believe that:

    * There is a positive correlation between efforts and performance,
    * Favorable performance will result in a desirable reward,
    * The rewardwill satisfy an important need,
    * The desire to satisfy the need is strong enough to make the
      effort worthwhile.
    * The theory is based upon the following beliefs:

    Valence
        refers to the emotional orientations people hold with respect
        to outcomes [rewards]. The depth of the want of an employee
        for extrinsic [money, promotion, time-off, benefits] or
        intrinsic [satisfaction] rewards). Management must discover
        what employees value.

    Expectancy
        employees have different expectations and levels of
        confidence about what they are capable of doing. Management
        must discover what resources, training, or supervision
        employees need.

    Instrumentality
        the perception of employees as to whether they will
        actually get what they desire even if it has been
        promised by a manager. Management must ensure that
        promises of rewards are fulfilled and that employees
        are aware of that.

    Vroom suggests that an employee's beliefs about Expectancy,
    Instrumentality, and Valence interact psychologically to create
    a motivational force such that the employee acts in ways that bring
    pleasure and avoid pain.
"""

from matplotlib.pyplot import show
from skfuzzy import trapmf

from numpy import arange
from skfuzzy import control as ctrl

expectancy = ctrl.Antecedent(arange(0, 100), "expectancy")
instrumentality = ctrl.Antecedent(arange(0, 100), "instrumentality")
valence = ctrl.Antecedent(arange(0, 100), "valence")
motivation = ctrl.Consequent(arange(0, 100), "motivation")

expectancy["low"] = trapmf(expectancy.universe, [0, 0, 25, 50])
expectancy["moderate"] = trapmf(expectancy.universe, [20, 40, 60, 80])
expectancy["high"] = trapmf(expectancy.universe, [50, 75, 100, 100])

instrumentality["low"] = trapmf(instrumentality.universe, [0, 0, 25, 50])
instrumentality["moderate"] = trapmf(instrumentality.universe, [20, 40, 60, 80])
instrumentality["high"] = trapmf(instrumentality.universe, [50, 75, 100, 100])

valence["low"] = trapmf(valence.universe, [0, 0, 25, 50])
valence["moderate"] = trapmf(valence.universe, [20, 40, 60, 80])
valence["high"] = trapmf(valence.universe, [50, 75, 100, 100])

motivation["low"] = trapmf(motivation.universe, [0, 0, 25, 50])
motivation["moderate"] = trapmf(motivation.universe, [20, 40, 60, 80])
motivation["high"] = trapmf(motivation.universe, [50, 75, 100, 100])

rule_1 = ctrl.Rule(
    expectancy["low"] & instrumentality["low"] & valence["low"],
    motivation["low"])

rule_2 = ctrl.Rule(
    expectancy["moderate"] & instrumentality["moderate"] & valence["moderate"],
    motivation["moderate"])

rule_3 = ctrl.Rule(
    expectancy["high"] & instrumentality["high"] & valence["high"],
    motivation["high"])

rules = [
    rule_1, rule_2, rule_3,
]

motivation_ctrl = ctrl.ControlSystem(rules)
motivation_simulador = ctrl.ControlSystemSimulation(motivation_ctrl)

if __name__ == "__main__":
    
    motivation_simulador.input["expectancy"] = int(input("Expectancy [0-100]: "))
    motivation_simulador.input["instrumentality"] = int(input("Instrumentality [0-100]: "))
    motivation_simulador.input["valence"] = int(input("Valence [0-100]: "))

    motivation_simulador.compute()
    print(f'Motivation: {motivation_simulador.output["motivation"]:.2f}%')
    
    motivation.view(sim=motivation_simulador); show()
