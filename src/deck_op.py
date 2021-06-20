from enum import Enum, auto
from typing import NoReturn


class Naipe(Enum):
    """Classe dos naipes."""

    ESPADAS = auto()  # E
    COPAS = auto()  # C
    PAUS = auto()  # P
    OUROS = auto()  # O


class Valor(Enum):
    """Classe dos valores."""

    DOIS = auto()
    TRES = auto()  # ou TRÊS
    QUATRO = auto()
    CINCO = auto()
    SEIS = auto()
    SETE = auto()
    OITO = auto()
    NOVE = auto()
    DEZ = auto()
    VALETE = auto()  # J
    DAMA = auto()  # Q
    REI = auto()  # K
    AS = auto()  # ou ÁS


class Carta:
    """Classe das cartas."""

    def __init__(self, valor: Valor, naipe: Naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f"<Carta {self.valor.name} de {self.naipe.name}>"

    @property
    def valor(self):
        """Atributo 'valor' protegido."""
        return self._valor

    @property
    def naipe(self):
        """Atributo 'naipe' protegido."""
        return self._naipe

    @valor.setter
    def valor(self, valor: Valor):
        if valor not in Valor:
            raise Exception("ERRO: valor inválido!")
        self._valor = valor

    @naipe.setter
    def naipe(self, naipe: Naipe):
        if naipe not in Naipe:
            raise Exception("ERRO: naipe inválido!")
        self._naipe = naipe


class Baralho:
    """Classe do baralho."""

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for valor in Valor for naipe in Naipe]

    def __getattr__(self, atributo):
        return None  # explícito é melhor do que implícito

    def __getitem__(self, posicao: int):
        return self.cartas[posicao]

    def __len__(self):
        return len(self.cartas)

    def __repr__(self):
        baralho = [f"{carta}\n" for carta in self.cartas]
        return "".join(baralho)

    def embaralhar(self) -> NoReturn:
        """Embaralha o baralho."""
        from random import shuffle

        shuffle(self.cartas)

    def pegar_carta(self) -> Carta:
        """Obtém uma carta aleatoriamente."""
        from random import randint

        if bool(len(self)):
            return self.cartas.pop(randint(0, len(self) - 1))
        raise Exception("Não há mais cartas disponíveis no baralho.")


class Mao:
    """Classe da mão do jogo de cartas."""

    _baralho = Baralho()

    def __init__(self, jogador: str, num_cartas: int = 5):
        self.__class__._baralho.embaralhar()
        self.jogador = jogador
        self.mao = [
            self.__class__._baralho.pegar_carta() for carta in range(num_cartas)
        ]

    def __len__(self):
        return len(self.mao)

    def __repr__(self):
        return f"{self.jogador}"

    def tirar_carta(self):
        """Tira uma carta aleatoriamente da mão do jogador."""
        from random import randint

        return self.mao.pop(randint(0, len(self) - 1))


if __name__ == "__main__":

    JOGADOR_1 = Mao("jogador_1")
    JOGADOR_2 = Mao("jogador_2")
