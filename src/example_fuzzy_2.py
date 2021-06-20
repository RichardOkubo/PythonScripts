def multiplica(mat_A: "matriz", mat_B: "matriz") -> "matriz":
    """Multiplica de Hadamard entre A com B."""
    assert len(mat_A) == len(mat_B) and len(mat_A[0]) == len(mat_B[0])
    matriz = [None] * len(mat_A)
    for linha in range(len(mat_A)):
        matriz[linha] = [None] * len(mat_A[0])
        for coluna in range(len(mat_A[0])):
            matriz[linha][coluna] = mat_A[linha][coluna] * mat_B[linha][coluna]
    return matriz


def transposta(matriz: "matriz") -> "matriz":
    """Cria uma matriz transposta da matriz dada pelo usuário."""
    matriz_transposta = []
    for coluna in range(len(matriz[0])):
        nova_coluna = []
        for linha in range(len(matriz)):
            nova_coluna.append(matriz[linha][coluna])
        matriz_transposta.append(nova_coluna)
    return matriz_transposta


def main(mat_A: "matriz", mat_B: "matriz", maximum=1211) -> float:
    """Função principal."""
    vetor = []
    matriz = transposta(multiplica(mat_A, mat_B))
    for vetor_ in matriz:
        vetor.append(sum(vetor_))
    return sum(vetor) / maximum


peso = [  # MODIFICADORES:
    [7, 8, 10, 10],  # muito importante
    [7, 8, 10, 10],  # muito importante
    [5, 6, 7, 8],  # importante
    [3, 4, 5, 6],  # moderadamente importante
    [3, 4, 5, 6],  # moderadamente importante
]

A = [  # CRITÉRIOS:
    [7, 8, 10, 10],  # muito desejável
    [5, 6, 8, 9],  # gostar
    [0, 1, 2, 3],  # muito caro
    [5, 6, 7, 8],  # versátil
    [1, 2, 2, 3],  # não veste bem
]

B = [  # CRITÉRIOS:
    [7, 8, 10, 10],  # muito desejável
    [5, 6, 8, 9],  # gostar
    [3, 4, 5, 6],  # caro
    [5, 6, 7, 8],  # versátil
    [1, 2, 2, 3],  # não veste bem
]

C = [  # CRITÉRIOS:
    [7, 8, 10, 10],  # muito desejável
    [5, 6, 8, 9],  # gostar
    [5, 6, 7, 8],  # coerente
    [5, 6, 7, 8],  # versátil
    [1, 2, 2, 3],  # não veste bem
]

D = [  # CRITÉRIOS:
    [7, 8, 10, 10],  # muito desejável
    [5, 6, 8, 9],  # gostar
    [8, 9, 10, 10],  # barato
    [5, 6, 7, 8],  # versátil
    [1, 2, 2, 3],  # não veste bem
]

produtos = [A, B, C, D]

if __name__ == "__main__":

    for produto in produtos:
        print(main(produto, peso))
