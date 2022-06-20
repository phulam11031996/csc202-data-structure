import unittest

import lab1


class Tests(unittest.TestCase):
    def test_max_none(self):
        with self.assertRaises(ValueError):
            lab1.max_iterative(None)

    def test_reverse_iterative_none(self):
        with self.assertRaises(ValueError):
            lab1.reverse_list_iterative(None)

    def test_reverse_recursive_none(self):
        with self.assertRaises(ValueError):
            lab1.reverse_list_recursive(None)

    # TODO: Add more tests!
    def test_max_iterative(self):
        self.assertEqual(lab1.max_iterative([]), None)

    def test_max_iterative2(self):
        self.assertEqual(lab1.max_iterative([-1, -3, 7, 2, 3, 4]), 7)

    def test_max_iterative3(self):
        self.assertEqual(lab1.max_iterative([1.2, 3.1, -1.4, 1]), 3.1)

    def test_reverse_list_iterative1(self):
        self.assertEqual(lab1.reverse_list_iterative(
            [1, 'a', -5, 'dog']),
            ['dog', -5, 'a', 1]
        )

    def test_reverse_list_iterative(self):
        self.assertEqual(lab1.reverse_list_iterative(
            [[1, 6], 1, 4, [], 5]),
            [5, [], 4, 1, [1, 6]]
        )

    def test_reverse_list_iterative2(self):
        self.assertEqual(lab1.reverse_list_recursive(
            [[1, 6], 1, 4, [], 5]),
            [5, [], 4, 1, [1, 6]]
        )

    def test_reverse_list_recursive(self):
        self.assertEqual(lab1.reverse_list_recursive(
            [1, 'a', -5, 'dog']),
            ['dog', -5, 'a', 1]
        )


if __name__ == '__main__':
    unittest.main()
