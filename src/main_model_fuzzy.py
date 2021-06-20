from random import choice

import dill

COR = ("feia", "normal", "bonita")
PRECO = ("caro", "coerente", "barato")
DESIGN = ("feio", "normal", "bonito")
MARCA = ("ruim", "indiferente", "boa")

AVALIACAO = ("irrelevante", "importante", "crucial")

MAXIMUM = (
    (3, 4, 5, 5),  # cor (valor máximo)
    (3, 4, 5, 5),  # preço (valor máximo)
    (3, 4, 5, 5),  # design (valor máximo)
    (3, 4, 5, 5),  # marca (valor máximo)
)


def modelo(arquivo: str = "modelo_fuzzy.pkl") -> callable:
    """Retorna a função 'fuzzy'."""
    with open("model_fuzzy.pkl", "rb") as f:
        fuzzy = dill.load(f)
    return fuzzy


def oferta(cor: str, preco: str, design: str, marca: str) -> "matriz":
    """Produz uma matriz oferda.

    Parâmetros:
        cor: ('feia', 'normal', 'bonita');
        preco: ('caro', 'coerente', 'barato');
        design: ('feio', 'normal', 'bonito');
        marca: ('ruim', 'indiferente', 'boa').
    Retorna:
        Uma matriz contendo listas de atributos fuzzy.
    """
    cor_ = {"feia": [1, 1, 2, 3], "normal": [2, 3, 3, 4], "bonita": [3, 4, 5, 5]}.get(
        cor
    )

    preco_ = {
        "caro": [1, 1, 2, 3],
        "coerente": [2, 3, 3, 4],
        "barato": [3, 4, 5, 5],
    }.get(preco)

    design_ = {
        "feio": [1, 1, 2, 3],
        "normal": [2, 3, 3, 4],
        "bonito": [3, 4, 5, 5],
    }.get(design)

    marca_ = {
        "ruim": [1, 1, 2, 3],
        "indiferente": [2, 3, 3, 4],
        "boa": [3, 4, 5, 5],
    }.get(marca)

    return [cor_, preco_, design_, marca_]


def demanda(f_cor: str, f_preco: str, f_design: str, f_marca: str) -> "matriz":
    """Produz uma matriz demanda.

    Retorna:
        Uma matriz contendo listas de avaliações fuzzy.

    * Precepções possíveis: ('irrelevante', 'importante', 'crucial').
    """

    def avaliacao(fator: str) -> list:
        return {
            "irrelevante": [1, 1, 2, 3],
            "importante": [2, 3, 3, 4],
            "crucial": [3, 4, 5, 5],
        }.get(fator)

    return [
        avaliacao(f_cor),
        avaliacao(f_preco),
        avaliacao(f_design),
        avaliacao(f_marca),
    ]


def apresentar(resultado: "matriz") -> "matriz":
    def transposta(matriz: list) -> list:
        """Cria uma matriz transposta da matriz dada pelo usuário."""
        matriz_transposta = []
        for coluna in range(len(matriz[0])):
            nova_coluna = []
            for linha in range(len(matriz)):
                nova_coluna.append(matriz[linha][coluna])
            matriz_transposta.append(nova_coluna)
        return matriz_transposta

    for i, linha in enumerate(transposta(resultado)):
        print(f"Cliente ({i+1})")
        for j, coluna in enumerate(linha):
            if j == len(linha) - 1:
                continue
            print(f"    Avaliação do produto ({j+1}): {coluna:.2f}")


def gerar_clientes_e_produtos(n_clientes: int = 1, n_produtos: int = 1) -> tuple:
    """Gera uma amostra de clientes e produtos com valores aleatórios."""
    clientes = []
    for _ in range(n_clientes):
        clientes.append(
            demanda(
                f_cor=choice(AVALIACAO),
                f_preco=choice(AVALIACAO),
                f_design=choice(AVALIACAO),
                f_marca=choice(AVALIACAO),
            )
        )
    produtos = []
    for _ in range(n_produtos):
        produtos.append(
            oferta(
                cor=choice(COR),
                preco=choice(PRECO),
                design=choice(DESIGN),
                marca=choice(MARCA),
            )
        )
    produtos.append(MAXIMUM)

    return clientes, produtos


if __name__ == "__main__":

    print("=" * 50)
    fuzzy = modelo(arquivo="modelo_fuzzy.pkl")
    while True:
        try:
            n_clientes = int(input("Gerar quantos clientes [int]: "))
            if n_clientes <= 0:
                print("    Digite um número inteiro maior do que zero.")
                continue
        except Exception:
            print("    Valor inválido!")
        else:
            break
    print()
    print()
    while True:
        try:
            n_produtos = int(input("Gerar quantos produtos [int]: "))
            if n_produtos <= 0:
                print("    Digite um número inteiro maior do que zero.")
                continue
        except Exception:
            print("    Valor inválido!")
        else:
            break
    clientes, produtos = gerar_clientes_e_produtos(
        n_clientes=n_clientes, n_produtos=n_produtos
    )
    print("-" * 50)
    apresentar(fuzzy(produtos, clientes, geral=True))
    print("=" * 50)
    input()
