def AOT(tabela_de_percepções_possíveis: dict = {}) -> callable:
    """Agente Orientado por Tabela (AOT).

    Este agente seleciona uma ação com base na sequência de percepção.
    É prático apenas para pequenos domínios.
    Para personalizá-lo, forneça como tabela um dicionário de todos pares
    possíveis.

    Ex:
        tabela = {
            ('A',): 1,
            ('A', 'B'): 2,
            ('A', 'B', 'C'): 3,
            ('A', 'C'): -2,
            ('A', 'C', 'B'): -3,
        }

        agente = AOT(tabela_de_percepções_possíveis=tabela)
        agente('A')  #  ->  1
        agente('C')  #  -> -2
        agente('B')  #  -> -3
        agente('C')  ## -> None

    """
    memória = []

    def programa(percepção: str) -> str:
        memória.append(percepção)
        ação = tabela_de_percepções_possíveis.get(tuple(memória))
        return ação

    return programa


if __name__ == "__main__":

    tabela = {
        ("A",): 1,
        ("A", "B"): 2,
        ("A", "B", "C"): 3,
        ("A", "C"): -2,
        ("A", "C", "B"): -3,
    }

    agente = AOT(tabela)
    print(agente("A"))
    print(agente("C"))
    print(agente("B"))

    input()
