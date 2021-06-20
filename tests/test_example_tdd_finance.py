"""Tests for the <finance> module.

This code was based on the book 'TDD: Test Guided Development' by Kent Beck.

I had to adapt the code - originally written in Java - for the Python language;
therefore, some features are not present in this file.
"""

from unittest import main, TestCase

from hodgepodge.example_tdd_finance import Bank, Money, Sum


class ExampleTDDFinanceTest(TestCase):

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.franc(5), Money.dollar(5))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum_ = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        sum_ = five.plus(five)
        self.assertEqual(five, sum_.augend)
        self.assertEqual(five, sum_.addend)

    def test_reduce_sum(self):
        sum_ = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        self.assertEqual(1, Bank().rate('USD', 'USD'))

    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        self.assertEqual(Money.dollar(10), result)

    def test_sum_plus_money(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum_ = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(15), result)

    def test_sum_times(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum_ = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum_, 'USD')
        self.assertEqual(Money.dollar(20), result)


if __name__ == '__main__':
    main()
