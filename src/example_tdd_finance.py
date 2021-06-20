"""Module <finance>.

This code was based on the book 'TDD: Test Guided Development' by Kent Beck.

I had to adapt the code - originally written in Java - for the Python language;
therefore, some features are not present in this file.
"""

# TODO(RichardOkubo): document the classes and methods.

from abc import ABC, abstractmethod
from typing import Dict, Tuple


class Expression(ABC):
    """Interface <Expression>."""

    @abstractmethod
    def plus(self, addend: 'Expression') -> 'Expression':
        """Abstract method <reduce>."""
        ...

    @abstractmethod
    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        """Abstract method <reduce>."""
        ...

    @abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        """Abstract method <reduce>."""
        ...


class Bank:
    """Class <Bank>."""

    def __init__(self):
        """Dunder <init>."""
        self._rates: Dict[Tuple[str], int] = dict()

    def add_rate(self, from_: str, to: str, rate: int):
        """Method <add_rate>."""
        self._rates[(from_, to)]: Dict[Tuple(str), int] = rate

    def rate(self, from_: str, to: str) -> int:
        """Method <rate>."""
        return 1 if from_ == to else self._rates[(from_, to)]

    def reduce(self, source: 'Expression', to: str) -> 'Money':
        """Method <reduce>."""
        return source.reduce(self, to)


class Money(Expression):
    """Class <Money>."""

    def __init__(self, amount: int, currency: str):
        """Dunder <init>."""
        self.amount: int = amount
        self._currency: int = currency

    def __repr__(self):
        """Dunder <repr>."""
        return f"Money({self.amount}, {self._currency})"

    def __eq__(self, other: 'Money'):
        """Dunder <eq>."""
        return (self.currency == other.currency and
                self.amount == other.amount)

    @property
    def currency(self):
        """Property for <self._currency>."""
        return self._currency

    @staticmethod
    def dollar(amount: int):
        """Static method <dollar>."""
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int):
        """Static method <franc>."""
        return Money(amount, 'CHF')

    def plus(self, addend: 'Expression') -> 'Expression':
        """Method <plus>."""
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        """Method <reduce>."""
        rate: int = bank.rate(self._currency, to)
        return Money(self.amount / rate, to)

    def times(self, multiplier: int) -> 'Expression':
        """Method <times>."""
        return Money(self.amount * multiplier, self._currency)


class Sum(Expression):
    """Class <Sum>."""

    def __init__(self, augend: 'Expression', addend: 'Expression'):
        """Dunder <init>."""
        self.augend: 'Expression' = augend
        self.addend: 'Expression' = addend

    def plus(self, addend: 'Expression') -> 'Expression':
        """Method <plus>."""
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        """Method <reduce>."""
        amount: int = (self.augend.reduce(bank, to).amount +
                       self.addend.reduce(bank, to).amount)
        return Money(amount, to)

    def times(self, multiplier: int) -> 'Expression':
        """Method <times>."""
        return Sum(self.augend.times(multiplier),
                   self.addend.times(multiplier))
