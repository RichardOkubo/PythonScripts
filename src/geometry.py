"""Module to draw regular polygons.

    When using the functions of this module, the python interpreter
will opena window with the drawing corresponding to the function
called by the user.

OBS:
    You may or may not import the <turtle> module. If used, it should
specify each function call with the named parameters.

Example in interactive python:
    >>> from turtle import Turtle
    >>> figura_geometrica = Turtle()
    >>> quadrado(figura_geometrica, 100)

Python script example:

    Importing Turtle from the <turtle> module:

    1. from geometria import arco
    2. from turtle import Turtle
    3.
    4. figura_geometrica = Turtle()
    5. arco(figura_geometrica, 100, 180)  # positional parameters
    6.
    7. mainloop()
    8.

    Without importing <turtle>:

    1. from geometria import poligono
    2.
    3. poligono(n_lados=3, comprimento=100)  # explaining parameters
    4.
    5. mainloop()
    6.
"""
from math import pi
from turtle import mainloop, Turtle


def poligono_linha(
    turtle_: Turtle = Turtle(),
    n_lados: int = 3,
    comprimento: float = 100,
    angulo: float = 90,
) -> None:
    """Draws lines / circumference of a polygon
    (auxiliary function).
    """
    for _ in range(n_lados):
        turtle_.fd(comprimento)
        turtle_.lt(angulo)


def poligono(
    turtle_: Turtle = Turtle(), n_lados: int = 3,
    comprimento: float = 100.0
) -> None:
    """Draws lines / circumference of a polygon
    (auxiliary function).
    """
    angulo = 360.0 / n_lados
    poligono_linha(turtle_, n_lados, comprimento, angulo)


def quadrado(
    turtle_: Turtle = Turtle(), comprimento: float = 100.0) -> None:
    """Draws a square."""
    for _ in range(4):
        turtle_.fd(comprimento)
        turtle_.lt(90)


def circulo(turtle_: Turtle = Turtle(), raio: float = 100.0) -> None:
    """Draws a circle."""
    arco(turtle_, raio, 360.0)


def arco(
    turtle_: Turtle = Turtle(), raio: float = 50.0, angulo: float = 180.0
    ) -> None:
    """Draws an arc."""
    comprimento_arco = 2 * pi * raio * angulo / 360
    n_lados_aproximado = int(comprimento_arco / 3) + 1
    comprimento_parcial = comprimento_arco / n_lados_aproximado
    angulo_parcial = angulo / n_lados_aproximado

    for _ in range(n_lados_aproximado):
        turtle_.fd(comprimento_parcial)
        turtle_.lt(angulo_parcial)


if __name__ == "__main__":

    BOB = Turtle()
    # quadrado(BOB, 100.0)
    # circulo(BOB, 100.0)
    # arco(BOB, 100.0, 180.0)
    poligono(BOB, 3, 100.0)

    mainloop()
