# import numpy as np
# import skfuzzy as fuzz
#
# from skfuzzy import control as ctrl
#
# design = ctrl.Antecedent(np.arange(1, 6), "design")
# potencia = ctrl.Antecedent(np.arange(1, 6), "potencia")
# economia = ctrl.Antecedent(np.arange(1, 6), "economia")
# preco = ctrl.Antecedent(np.arange(1, 6), "preco")
# espaco = ctrl.Antecedent(np.arange(1, 6), "espaco")
#
# percepcao = ctrl.Consequent(np.arange(1, 6), "percepcao")
#
# # Design
# design["feio"] = fuzz.trapmf(design.universe, [1, 1, 2, 3])
# design["razoável"] = fuzz.trapmf(design.universe, [2, 3, 3, 4])
# design["belo"] = fuzz.trapmf(design.universe, [3, 4, 5, 5])
#
# # Potência
# potencia["baixa"] = fuzz.trapmf(potencia.universe, [1, 1, 2, 3])
# potencia["média"] = fuzz.trapmf(potencia.universe, [2, 3, 3, 4])
# potencia["alta"] = fuzz.trapmf(potencia.universe, [3, 4, 5, 5])
#
# # Economia
# economia["baixa"] = fuzz.trapmf(economia.universe, [1, 1, 2, 3])
# economia["média"] = fuzz.trapmf(economia.universe, [2, 3, 3, 4])
# economia["alta"] = fuzz.trapmf(economia.universe, [3, 4, 5, 5])
#
# # Preço
# preco["elevado"] = fuzz.trapmf(preco.universe, [1, 1, 2, 3])
# preco["coerente"] = fuzz.trapmf(preco.universe, [2, 3, 3, 4])
# preco["barato"] = fuzz.trapmf(preco.universe, [3, 4, 5, 5])
#
# # Espaço Interno
# espaco["apertado"] = fuzz.trapmf(espaco.universe, [1, 1, 2, 3])
# espaco["médio"] = fuzz.trapmf(espaco.universe, [2, 3, 3, 4])
# espaco["espaçoso"] = fuzz.trapmf(espaco.universe, [3, 4, 5, 5])
#
# # Percepção
# percepcao["dispensável"] = fuzz.trapmf(percepcao.universe, [1, 1, 2, 3])
# percepcao["importante"] = fuzz.trapmf(percepcao.universe, [2, 3, 3, 4])
# percepcao["crucial"] = fuzz.trapmf(percepcao.universe, [3, 4, 5, 5])

from pprint import pprint


def multiplica(mat_A: "matriz", mat_B: "matriz") -> "matriz":
    """Multiplica as matrizes A com B."""
    assert len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0])
    matriz = [None] * len(mat_A)
    for linha in range(len(mat_A)):
        matriz[linha] = [None] * len(mat_A[0])
        for coluna in range(len(mat_A[0])):
            matriz[linha][coluna] = mat_A[linha][coluna] * mat_B[linha][coluna]
    return matriz


def reduz(matriz: "matriz") -> int:
    """Reduz a matriz em um número, que é a soma de cada elemento da matriz."""
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma


def transposta(matriz: "matriz") -> "matriz":
    """Cria uma matriz transposta da matriz dada pelo usuário."""
    matriz_transposta = []
    for coluna in range(len(matriz[0])):
        nova_coluna = []
        for linha in range(len(matriz)):
            nova_coluna.append(matriz[linha][coluna])
        matriz_transposta.append(nova_coluna)
    return matriz_transposta


# ------------------------------------------------------------------------------
def oferta_demanda(oferta: list, demanda: list) -> list:
    """Função de cruzamento entre oferta e demanda."""
    resultado = []
    for oferta_ in oferta:
        resultado.append(reduz(multiplica(oferta_, demanda)))
    return resultado


def normalizador(matriz: list) -> list:
    """Normaliza os valores da matriz passada."""
    matriz_normalizada = []
    maximizante_da_matriz = matriz[-1]
    for linha in matriz:
        nova_coluna = []
        for i, coluna in enumerate(linha):
            nova_coluna.append(coluna / maximizante_da_matriz[i])
        matriz_normalizada.append(nova_coluna)
    return matriz_normalizada


def resolve(oferta: list, demanda: (list, "matriz"), geral=False) -> "matriz":
    """Função que resolve tanto para um ou mais clientes passado."""
    resultado_parcial = []

    if not geral:
        resultado_parcial.append(oferta_demanda(oferta, demanda))
    else:
        for i in range(len(demanda)):
            resultado_parcial.append(oferta_demanda(oferta, demanda[i]))

    resultado_final = normalizador(transposta(resultado_parcial))
    return resultado_final


# ------------------------------------------------------------------------------
# CARROS
produto_A = [
    [1, 1, 2, 3],  # design - feio
    [1, 1, 2, 3],  # potência - baixa
    [3, 4, 5, 5],  # economia - alta
    [3, 4, 5, 5],  # preço - barato
    [1, 1, 2, 3],  # espaço - apertado
]
produto_B = [[3, 4, 5, 5], [3, 4, 5, 5], [1, 1, 2, 3], [1, 1, 2, 3], [3, 4, 5, 5]]
produto_C = [[2, 3, 3, 4], [2, 3, 3, 4], [2, 3, 3, 4], [2, 3, 3, 4], [3, 4, 5, 5]]
produto_D = [[3, 4, 5, 5], [3, 4, 5, 5], [1, 1, 2, 3], [1, 1, 2, 3], [2, 3, 3, 4]]

# MAXIMIZANTE
maximizante = [  # Máximos valores possíveis para cada atributo de produto
    [3, 4, 5, 5],
    [3, 4, 5, 5],
    [3, 4, 5, 5],
    [3, 4, 5, 5],
    [3, 4, 5, 5],
]

# CLIENTES
cliente_A = [
    [2, 3, 3, 4],  # design - importante
    [3, 4, 5, 5],  # potência - crucial
    [2, 3, 3, 4],  # economia - importante
    [2, 3, 3, 4],  # preço - importante
    [3, 4, 5, 5],  # espaço - crucial
]
cliente_B = [
    [2, 3, 3, 4],  # design - importante
    [3, 4, 5, 5],  # potência - crucial
    [1, 1, 2, 3],  # economia - dispensável
    [1, 1, 2, 3],  # preço - dispensável
    [1, 1, 2, 3],  # espaço - dispensável
]
cliente_C = [
    [1, 1, 2, 3],  # design - dispensável
    [2, 3, 3, 4],  # potência - importante
    [2, 3, 3, 4],  # economia - importante
    [2, 3, 3, 4],  # preço - importante
    [3, 4, 5, 5],  # espaço - crucial
]
cliente_D = [
    [1, 1, 2, 3],  # design - dispentável
    [1, 1, 2, 3],  # potência - dispensável
    [3, 4, 5, 5],  # economia - crucial
    [3, 4, 5, 5],  # preço - crucial
    [1, 1, 2, 3],  # espaço - dispensável
]

produtos = [produto_A, produto_B, produto_C, produto_D, maximizante]
clientes = [cliente_A, cliente_B, cliente_C, cliente_D]

if __name__ == "__main__":

    pprint(resolve(oferta=produtos, demanda=cliente_A, geral=False))
