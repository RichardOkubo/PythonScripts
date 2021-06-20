from functools import wraps
from numbers import Number


def validar(funcao):
    @wraps(funcao)
    def inner(x, y):
        if isinstance(x, funcao.__annotations__["x"]) and isinstance(
            y, funcao.__annotations__["y"]
        ):
            return funcao(x, y)
        return None

    return inner


@validar
def soma(x: Number, y: Number) -> Number:
    return x + y
