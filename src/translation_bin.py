"""Módulo para codificar e decodificar uma mensagem (pt-br/números binários).

Contém as seguintes funções:
    - codificar
    - decodificar
"""

__version__ = "0.0.1"
__author__ = "Richard Okubo"

from re import findall
from typing import List


def codificar(mensagem: str) -> str:
    """Função que codifica uma linguagem humana (ex: pt-br) em código binário.

    EXEMPLO:
        >>> mensagem: str = 'Hello, world!'
        >>> codificar(mensagem)
        ::: '0100100001100101011011000110110001101111001011000010000001110111011
            0111101110010011011000110010000100001'
    """

    caracteres: List[str] = findall(".", mensagem)
    bytes: List[str] = []

    for caracter in caracteres:
        bits: str = bin(ord(caracter))[2:]  # Códico binário (parcial)

        while len(bits) < 8:
            bits = "0" + bits

        bytes.append(bits)
    codigo: str = str().join(bytes)

    return codigo


def decodificar(codigo: str) -> str:
    """Função que decodifica uma mensagem binário em linguagem humana.

    EXEMPLO:
        >>> codigo: str = '01001000011001010110110001101100011011110010110000100
                           000011101110110111101110010011011000110010000100001'
        >>> decodificar(codigo)
        ::: 'Hello, world!'
    """

    bytes: List[str] = findall("........", codigo)
    decimais: List[int] = []

    for byte in bytes:
        decimal: int = sum(int(bit) * 2 ** i for i, bit in enumerate(reversed(byte)))
        decimais.append(decimal)

    caracteres: List[str] = [chr(decimal) for decimal in decimais]
    mensagem: str = str().join(caracteres)

    return mensagem


if __name__ == "__main__":

    while True:
        print(codificar(input("> ")), end="\n\n")
