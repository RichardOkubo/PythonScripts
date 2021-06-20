def main(oferta: list, demanda: (list, "matriz"), geral=False) -> "matriz":
    """Resolve tanto para um ou mais clientes passado.

    params:
        oferta (list): lista de produtos (cada produto em formato de matriz);
        demanda (list ou matriz): lista ou matriz de clientes (bis);
        geral (bool): 'True' caso esteja trabalhando com uma lista de clientes.
    return: matriz com valores das avaliações.
    """

    def oferta_demanda(oferta: list, demanda: list) -> list:
        """Função de cruzamento entre oferta e demanda."""

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

        resultado = []
        for oferta_ in oferta:
            resultado.append(reduz(multiplica(oferta_, demanda)))
        return resultado

    def transposta(matriz: "matriz") -> "matriz":
        """Cria uma matriz transposta da matriz dada pelo usuário."""
        matriz_transposta = []
        for coluna in range(len(matriz[0])):
            nova_coluna = []
            for linha in range(len(matriz)):
                nova_coluna.append(matriz[linha][coluna])
            matriz_transposta.append(nova_coluna)
        return matriz_transposta

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

    resultado_parcial = []

    if not geral:
        resultado_parcial.append(oferta_demanda(oferta, demanda))
    else:
        for i in range(len(demanda)):
            resultado_parcial.append(oferta_demanda(oferta, demanda[i]))

    resultado_final = normalizador(transposta(resultado_parcial))
    return resultado_final


if __name__ == "__main__":
    # CARROS
    produto_A = [
        [1, 1, 2, 3],  # design - feio
        [1, 1, 2, 3],  # potência - baixa
        [3, 4, 5, 5],  # economia - alta
        [3, 4, 5, 5],  # preço - barato
        [1, 1, 2, 3],  # espaço - apertado
    ]
    produto_B = [
        [3, 4, 5, 5],  # design - feio
        [3, 4, 5, 5],  # potência - baixa
        [1, 1, 2, 3],  # economia - alta
        [1, 1, 2, 3],  # preço - barato
        [3, 4, 5, 5]   # espaço - apertado
    ]
    produto_C = [
        [2, 3, 3, 4],  # design - feio
        [2, 3, 3, 4],  # potência - baixa
        [2, 3, 3, 4],  # economia - alta
        [2, 3, 3, 4],  # preço - barato
        [3, 4, 5, 5]   # espaço - apertado
    ]
    produto_D = [
        [3, 4, 5, 5],  # design - feio
        [3, 4, 5, 5],  # potência - baixa
        [1, 1, 2, 3],  # economia - alta
        [1, 1, 2, 3],  # preço - barato
        [2, 3, 3, 4]   # espaço - apertado
    ]
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

    # from pprint import pprint
    # pprint(main(oferta=produtos, demanda=cliente_A, geral=False))
    # input()

    import dill

    with open("model_fuzzy.pkl", "wb") as f:
        dill.dump(main, f)
