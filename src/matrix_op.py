"""Módulo de operações com matrizes."""
from math import exp
from random import randint


def aplica(funcao: callable = lambda x: x, matriz: list = []) -> list:
    """Aplica uma função definida pelo usuário para cada elemento da matriz."""
    nova_matriz = []
    for linha in range(len(matriz)):
        nova_coluna = [funcao(x) for x in matriz[linha]]
        nova_matriz.append(nova_coluna)
    return nova_matriz


def divide(mat_A: list, mat_B: list) -> list:
    """Aplica a divisão de Hadamard entre as matrizes A e B."""
    assert len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0])
    matriz = [None] * len(mat_A)
    for linha in range(len(mat_A)):
        matriz[linha] = [None] * len(mat_A[0])
        for coluna in range(len(mat_A[0])):
            assert mat_B[linha][coluna] != 0
            matriz[linha][coluna] = mat_A[linha][coluna] / mat_B[linha][coluna]
    return matriz


def exponencial(matriz: list = []) -> list:
    """Aplica uma função 'exp' para cada elemento da matriz."""
    nova_matriz = []
    for linha in matriz:
        nova_coluna = []
        for coluna in linha:
            nova_coluna.append(exp(coluna))
        nova_matriz.append(nova_coluna)
    return nova_matriz


def matriz_identidade(ordem: int = 1) -> list:
    """Cria uma matriz identidade."""
    matriz = []
    for linha in range(ordem):
        nova_coluna = []
        for coluna in range(ordem):
            nova_coluna.append(0) if linha != coluna else nova_coluna.append(1)
        matriz.append(nova_coluna)
    return matriz


def matriz_nula(n_linhas: int = 1, n_colunas: int = 1) -> list:
    """Cria uma matriz nula."""
    matriz = [0] * n_linhas
    for i in range(n_linhas):
        matriz[i] = [0] * n_colunas
    return matriz


def matriz_randomica(
    n_linhas: int = 1, n_colunas: int = 1, funcao: callable = randint, de=-10, a=10
) -> list:
    """Cria uma matriz com valores (inteiros) aleatórios."""
    matriz = []
    for linha in range(n_linhas):
        nova_coluna = []
        for coluna in range(n_colunas):
            nova_coluna.append(funcao(de, a))
        matriz.append(nova_coluna)
    return matriz


def matriz_vazia(n_linhas: int = 1, n_colunas: int = 1) -> list:
    """Cria uma matriz vazia (com valor 'None')."""
    matriz = [None] * n_linhas
    for i in range(n_linhas):
        matriz[i] = [None] * n_colunas
    return matriz


def multiplica(mat_A: list, mat_B: list) -> list:
    """Aplica o produto de Hadamard entre as matrizes A e B."""
    assert len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0])
    matriz = [None] * len(mat_A)
    for linha in range(len(mat_A)):
        matriz[linha] = [None] * len(mat_A[0])
        for coluna in range(len(mat_A[0])):
            matriz[linha][coluna] = mat_A[linha][coluna] * mat_B[linha][coluna]
    return matriz


def produto_escalar(escalar: float, matriz: list) -> list:
    """Aplica o produto escalar entre um número e uma matriz."""
    nova_matriz = [None] * len(matriz)
    for linha in range(len(matriz)):
        nova_matriz[linha] = [None] * len(matriz[0])
        for coluna in range(len(matriz[0])):
            nova_matriz[linha][coluna] = escalar * matriz[linha][coluna]
    return nova_matriz


def produto_vetorial(mat_A: list, mat_B: list) -> list:
    """Aplica uma multiplicação matricial entre A e B."""
    assert len(mat_A[0]) == len(mat_B)
    matriz = []
    for linha in range(len(mat_A)):
        matriz.append([])
        for coluna in range(len(mat_B[0])):
            matriz[linha].append(0)
            for k in range(len(mat_A[0])):
                matriz[linha][coluna] += mat_A[linha][k] * mat_B[k][coluna]
    return matriz


def reduz(matriz: list) -> int:
    """Reduz a matriz em um número, que é a soma de cada elemento da matriz."""
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma


def soma(mat_A: list, mat_B: list) -> list:
    """Soma as matrizes A com B."""
    assert len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0])
    matriz = [None] * len(mat_A)
    for linha in range(len(mat_A)):
        matriz[linha] = [None] * len(mat_A[0])
        for coluna in range(len(mat_A[0])):
            matriz[linha][coluna] = mat_A[linha][coluna] + mat_B[linha][coluna]
    return matriz


def subtrai(mat_A: list, mat_B: list) -> list:
    """Subrai as matrizes A com B."""
    assert len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0])
    matriz = [None] * len(mat_A)
    for linha in range(len(mat_A)):
        matriz[linha] = [None] * len(mat_A[0])
        for coluna in range(len(mat_A[0])):
            matriz[linha][coluna] = mat_A[linha][coluna] - mat_B[linha][coluna]
    return matriz


def transforma(
    vetor: list, matriz_linha: bool = True, T: callable = lambda x: transposta(x)
) -> list:
    """Transforma um vetor em uma matriz linha ou matriz coluna."""
    matriz = []
    if matriz_linha:
        matriz.append(vetor)
    else:
        matriz.append(vetor)
        matriz = T(matriz)
    return matriz


def transposta(matriz: list) -> list:
    """Cria uma matriz transposta da matriz dada pelo usuário."""
    matriz_transposta = []
    for coluna in range(len(matriz[0])):
        nova_coluna = []
        for linha in range(len(matriz)):
            nova_coluna.append(matriz[linha][coluna])
        matriz_transposta.append(nova_coluna)
    return matriz_transposta
