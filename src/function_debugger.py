from functools import wraps
from logging import basicConfig, DEBUG, debug as debug_


def debug(function):
    """Decorator that debugs any function.
    
    Write the logs in the file 'log.log' with the
    parameters and the return of the debugged function.
    """

    basicConfig(
        filename="log.log",
        level=DEBUG,
        filemode="w",
        format="%(message)s",
    )

    @wraps(function)
    def inner(*args, **kwargs):
        debug_(f"FUNCTION: {function.__name__}")
        debug_(f"IN: \targs{args}\tkwargs{kwargs}")
        result = function(*args, **kwargs)
        debug_(f"OUT:\t{result}\n")
        return result

    return inner
