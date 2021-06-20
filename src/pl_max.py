"""Programação linear com Python (Maximização).

max z = 5*x1 + 7*x2

sujeito a:

      x1        <= 16
    2*x1 + 3*x2 <= 19
      x1 +   x2 <= 8
      x1,    x2 >= 0
"""
import numpy as np
from scipy.optimize import linprog

# Defina a matriz de restrições de desigualdade
# OBS: as restrições de desigualdade devem estar na forma de <=
A = np.array([[1, 0], [2, 3], [1, 1], [-1, 0], [0, -1]])

# Defina o vetor de restrições de desigualdade
b = np.array([16, 19, 8, 0, 0])

# Defina os coeficientes do vetor de função objetivo linear
# OBS: ao maximizar, altere os sinais do coeficiente do vetor c
c = np.array([-5, -7])

# Resolução do problema de programação linear
k = linprog(c=c, A_ub=A, b_ub=b)

# Resultados
print(
    f"""
    Valor ótimo: {round(k.fun, ndigits=2)}
    valores de x: {k.x}
    Número de iterações realizadas: {k.nit}
    Status: {k.message}
    """
)
