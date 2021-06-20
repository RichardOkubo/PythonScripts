from functools import wraps
from typing import Callable


def idioma(linguagem: str) -> Callable:
    """Seleciona o idioma"""
    saldações = {"pt": "Olá", "en": "Hello", "ge": "Hallo"}

    def externa(saldar_: Callable) -> Callable:
        """Decorador para função <saldar>"""

        @wraps
        def interna(nome: str) -> str:
            return saldar_(nome, saldações[linguagem])

        return interna

    return externa


@idioma("ge")
def saldar(nome: str, saldação: str = None) -> str:
    return f"{saldação}, {nome}!"


if __name__ == "__main__":
    print(saldar("Richard"))
