import unittest

import sample


class Tests(unittest.TestCase):
    def test_factorial0(self):
        self.assertEqual(sample.factorial(0), 1)

    def test_factorial1(self):
        self.assertEqual(sample.factorial(1), 1)

    def test_factorial2(self):
        self.assertEqual(sample.factorial(2), 2)

    def test_factorial3(self):
        self.assertEqual(sample.factorial(3), 6)

    def test_factorial10(self):
        self.assertEqual(sample.factorial(10), 3628800)

    # NOTE: This is how you can test for when an error should be raised.
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            sample.factorial(-5)

    def test_fibonacci0(self):
        self.assertEqual(sample.fibonacci(0), 0)

    def test_fibonacci1(self):
        self.assertEqual(sample.fibonacci(1), 1)

    def test_fibonacci2(self):
        self.assertEqual(sample.fibonacci(2), 1)

    def test_fibonacci3(self):
        self.assertEqual(sample.fibonacci(3), 2)

    def test_fibonacci10(self):
        self.assertEqual(sample.fibonacci(10), 55)

    # NOTE: This is how you can test for when an error should be raised.
    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            sample.fibonacci(-5)

    def test_max_recursive1(self):
        self.assertEqual(sample.max_recursive([1, 2, 3, 4]), 4)

    def test_max_recursive2(self):
        self.assertEqual(sample.max_recursive([1, 2, 4, 3]), 4)

    def test_max_recursive3(self):
        self.assertEqual(sample.max_recursive([1, 4, 2, 3]), 4)

    def test_max_recursive4(self):
        self.assertEqual(sample.max_recursive([4, 1, 2, 3]), 4)

    def test_max_recursive5(self):
        self.assertEqual(sample.max_recursive([-9, -4, -1, -100, -4]), -1)

    def test_max_recursive_empty(self):
        self.assertIsNone(sample.max_recursive([]))

    def test_reverse_string_iterative1(self):
        self.assertEqual(sample.reverse_string_iterative(''), '')

    def test_reverse_string_iterative2(self):
        self.assertEqual(sample.reverse_string_iterative('abcd'), 'dcba')


if __name__ == '__main__':
    unittest.main()
