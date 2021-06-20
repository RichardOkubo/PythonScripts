from numbers import Number
from random import gauss
from typing import Callable, List, NewType

NumericArray1D = NewType("NumericArray1D", List[Number])
NumericArray2D = NewType("NumericArray2D", List[List[Number]])
Function = NewType("Function", Callable[[Number], Number])


def step_function(u: Number) -> Number:
    return 1 if u >= 0 else 0


class Perceptron:
    def __init__(self, X: NumericArray2D, Y: NumericArray2D, eta: float = 0.1,
                 epoch: int=1000, b: Number=1, show: bool=False,
                 activation_function: Function=step_function):
        self.X: NumericArray2D = X
        self.Y: NumericArray2D = Y
        self.eta: float = eta
        self.epoch: int = epoch
        self.b: Number = b
        self.N: int = len(X)
        self.n: int = len(X[0])
        self.w: NumericArray1D = []
        self.show: bool = show
        self.activation_function: Function = activation_function

    def train(self):
        for x in self.X:
            x.insert(0, self.b)

        for i in range(self.n + 1):
            self.w.append(gauss(mu=0.0, sigma=1.0))

        n_epoch: int = 1
        
        while True:

            if self.show:
                print(f"Epoch:  {n_epoch}\tWeight:  {self.w}")

            erro: bool = False

            for i in range(self.N):
                u: Number = sum(self.w[j] * self.X[i][j] for j in range(self.n + 1))
                d: Number = self.activation_function(u)

                if d != self.Y[i]:
                    for j in range(self.n + 1):
                        self.w[j] += self.eta * (self.Y[i]-d) * self.X[i][j]

                    erro = True
            n_epoch += 1

            if n_epoch > self.epoch or not erro:
                break


def predict(perceptron: Perceptron, X: NumericArray2D) -> Number:
    return perceptron.activation_function(
        sum(perceptron.w[i] * X[i] for i in range(len(X))))
