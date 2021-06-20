"""Programação linear com Python (Minimização).

min z = 10*x1 + 15*x2 + 25*x3

sujeito a:

    x1 +   x2 + x3 >= 1000
    x1 - 2*x2      >= 0
                x3 >= 340
    x1,    x2,  x3 >= 0
"""
import numpy as np
from scipy.optimize import linprog

# Defina a matriz de restrições de desigualdade
# OBS: as restrições de desigualdade devem estar na forma de <=
A = np.array([[-1, -1, -1], [-1, 2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])

# Defina o vetor de restrições de desigualdade
b = np.array([-1000, 0, -340, 0, 0, 0])

# Defina os coeficientes do vetor de função objetivo linear
c = np.array([10, 15, 25])

# Resolução do problema de programação linear
k = linprog(c=c, A_ub=A, b_ub=b, method="simplex")

# Resultados
# Resultados
print(
    f"""
    Valor ótimo: {round(k.fun, ndigits=2)}
    valores de x: {k.x}
    Número de iterações realizadas: {k.nit}
    Status: {k.message}
    """
)
