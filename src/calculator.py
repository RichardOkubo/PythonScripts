"""Simple calculator."""

import operator
from functools import wraps


def validate(function: callable) -> callable:
    @wraps(function)
    def inner(x: int, y: int) -> int:
        if isinstance(x, int) and isinstance(y, int):
            return function(x, y)
        raise Exception("All arguments must be integers.")
    return inner


@validate
def add(x: int = 0, y: int = 0, function: callable = operator.add) -> int:
    return function(x, y)


@validate
def sub(x: int = 0, y: int = 0, function: callable = operator.sub) -> int:
    return function(x, y)


@validate
def mul(x: int = 0, y: int = 0, function: callable = operator.mul) -> int:
    return function(x, y)


@validate
def div(x: int = 0, y: int = 0, function: callable = operator.truediv) -> float:
    return function(x, y)
