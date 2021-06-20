"""Módulo para validador de entradas numéricas."""

from functools import wraps
from numbers import Number
from typing import Callable, Tuple


def validador(funcao: Callable) -> Callable:
    """Decorador para validação numérica."""

    @wraps(funcao)
    def inner(*args: Tuple[Number]) -> Callable:
        if all(
            isinstance(valor, funcao.__annotations__[chave])
            for chave, valor in funcao.__annotations__.items()
        ):  # Arrumar
            return funcao(sum(args))
        return None

    return inner


@validador
def soma(x: Number, y: Number) -> Number:
    """Função que soma qualquer número."""
    return x + y
