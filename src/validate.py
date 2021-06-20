"""Module to validate type annotations in functions."""

# TODO(RichardOkubo):
# - Criar opção para especificar o tipo de retorno caso não seja validado.
# - Criar as exceções <StrictlyNamedError> e <TypeHintsError>.
# * Usar o decorador com parâmetro.

__version__ = "0.1.0"
__author__ = "Richard Okubo"

from functools import wraps
from numbers import Number
from typing import Callable, Dict


def validate(function: Callable) -> Callable:
    """Decorate a function to validate any type annotations.

    Args:
        function: any functions.

    Returns:
        The function passed, but incorporated with the type annotation
        validator. For exampla:

        >>> from decorator import validate
        >>> @validate
        ... def add(x: Number, y: Number, /) -> Number:
        ...     # Add any two numbers.
        ...     return x + y
        >>> add(x=1, y=2)
        3
        >>> add(x='hello', y=2)  # Return None
        >>>

    Raises:
        StrictlyNamedError: The arguments passed to the decorated function
          must be strictly named. Otherwise, the decorator will not
          work. For exempla:

          <continuation>
          >>> add(1, 2)
          <or>
          >>> add(x=2, 2)  # Raise FooError

        TypeHintsError: Type hints must be used. Otherwise, the
          decorator will not work.
    """

    @wraps(function)
    def inner(**kwargs: Dict[str, Number]) -> Callable:
        if all(
            isinstance(kwargs[key], type)
            for key, type in function.__annotations__.items()
            if key != "return"
        ):
            return function(*kwargs.values())
        return None

    return inner


# from typing import Any, Callable, Dict, Tuple, Union
#
#
# def validate_type(type: Any = None, standard_return: Any = None) -> Callable:
#     def validate(function: Callable) -> Callable:
#         def inner(*args: Tuple, **kwargs: Dict) -> Union[Callable, Any]:
#             if all(isinstance(value, type) for value in kwargs.values()):
#                 return function(*args, **kwargs)
#             return standard_return
#
#         return inner
#
#     return validate
#
#
# @validate_type(type=int, standard_return=-1)
# def add_two_interger(x: int, y: int) -> int:
#     "Add two interger."
#     return x + y


if __name__ == "__main__":
    print(__doc__)
