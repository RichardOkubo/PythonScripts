"""Simple example of Unit tests."""

from unittest import TestCase, main

from hodgepodge.calculator import add, div, mul, sub


class TestCalculadora(TestCase):

    def test_add_int_with_int(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(-1, 0), -1)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1, -2), -3)

    def test_add_int_with_str(self):
        with self.assertRaises(Exception):
            add(1, 'eraser')
            add('pencil', 1)
            add('pencil', 'eraser')

    def test_add_int_with_float(self):
        with self.assertRaises(Exception):
            add(1, 1.1)
            add(1.1, 1)
            add(1.1, 1.1)

    def test_sub_int_with_int(self):
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(1, 0), 1)
        self.assertEqual(sub(1, -1), 2)
        self.assertEqual(sub(-1, 0), -1)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(-1, -2), 1)

    def test_sub_int_with_str(self):
        with self.assertRaises(Exception):
            sub(1, 'eraser')
            sub('pencil', 1)
            sub('pencil', 'eraser')

    def test_sub_int_with_float(self):
        with self.assertRaises(Exception):
            sub(1, 1.1)
            sub(1.1, 1)
            sub(1.1, 1.1)

    def test_mul_int_with_int(self):
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(1, 1), 1)
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(1, -1), -1)
        self.assertEqual(mul(-1, 0), 0)
        self.assertEqual(mul(-1, -1), 1)
        self.assertEqual(mul(-1, -2), 2)

    def test_mul_int_with_str(self):
        with self.assertRaises(Exception):
            mul(1, 'eraser')
            mul('pencil', 1)
            mul('pencil', 'eraser')

    def test_mul_int_with_float(self):
        with self.assertRaises(Exception):
            mul(1, 1.1)
            mul(1.1, 1)
            mul(1.1, 1.1)

    def test_div_int_with_int(self):
        self.assertEqual(div(1, 2), 0.5)
        self.assertEqual(div(1, 1), 1)
        self.assertEqual(div(1, -1), -1)
        self.assertEqual(div(-1, -1), 1)
        self.assertEqual(div(-1, -2), 0.5)

    def test_div_int_with_str(self):
        with self.assertRaises(Exception):
            mul(1, 'eraser')
            mul('pencil', 1)
            mul('pencil', 'eraser')

    def test_div_int_with_float(self):
        with self.assertRaises(Exception):
            mul(1, 1.1)
            mul(1.1, 1)
            mul(1.1, 1.1)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(div(1, 0), 0)
            self.assertEqual(div(-1, 0), 0)
            self.assertEqual(div(0, 0), 0)


if __name__ == '__main__':
    main()
