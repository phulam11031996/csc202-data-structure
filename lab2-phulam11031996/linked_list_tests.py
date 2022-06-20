import unittest

from linked_list import (
    Pair, empty_list, add, length, get, setitem, remove)


class Tests(unittest.TestCase):
    # NOTE: This does not test for any sort of correctness (writing
    # those tests will be your job!), this only makes sure that all of
    # the functions exist by the correct names and can be called with
    # valid parameters.
    def test_function_names(self):
        my_list = empty_list()
        my_list = add(my_list, 0, 'Hello!')
        length(my_list)
        get(my_list, 0)
        my_list = setitem(my_list, 0, 'Bye!')
        value, my_list = remove(my_list, 0)

    # TODO: Add more tests!

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add(self):
        test_list = Pair(1, Pair(2, Pair(3, Pair(4, None))))

        self.assertEqual(
            add(test_list, 0, 'a'),
            Pair('a', Pair(1, Pair(2, Pair(3, Pair(4, None)))))
            )
        self.assertEqual(
            add(test_list, 1, 'a'),
            Pair(1, Pair('a', Pair(2, Pair(3, Pair(4, None)))))
            )
        self.assertEqual(
            add(test_list, 4, 'a'),
            Pair(1, Pair(2, Pair(3, Pair(4, Pair('a', None)))))
            )

        with self.assertRaises(IndexError):
            add(test_list, -1, 'a')
        with self.assertRaises(IndexError):
            add(test_list, 5, 'a')

    def test_length(self):
        test_list = Pair(1, Pair(2, Pair(3, Pair(4, None))))
        self.assertEqual(length(test_list), 4)

    def test_get(self):
        test_list = Pair(1, Pair(2, Pair(3, Pair(4, None))))

        self.assertEqual(get(test_list, 0), 1)
        self.assertEqual(get(test_list, 1), 2)
        self.assertEqual(get(test_list, 2), 3)

        with self.assertRaises(IndexError):
            get(test_list, -1)
        with self.assertRaises(IndexError):
            get(test_list, 4)

    def test_setitem(self):
        test_list = Pair(1, Pair(2, Pair(3, Pair(4, None))))

        self.assertEqual(
            setitem(test_list, 0, 'a'),
            Pair('a', Pair(2, Pair(3, Pair(4, None))))
            )
        self.assertEqual(
            setitem(test_list, 1, 'a'),
            Pair(1, Pair('a', Pair(3, Pair(4, None))))
            )
        self.assertEqual(
            setitem(test_list, 2, 'a'),
            Pair(1, Pair(2, Pair('a', Pair(4, None))))
            )

        with self.assertRaises(IndexError):
            setitem(test_list, -1, 'a')
        with self.assertRaises(IndexError):
            setitem(test_list, 4, 'a')

    def test_remove(self):
        test_list = Pair(1, Pair(2, Pair(3, Pair(4, None))))
        self.assertEqual(
            remove(test_list, 0),
            (1, Pair(2, Pair(3, Pair(4, None))))
            )
        self.assertEqual(
            remove(test_list, 1),
            (2, Pair(1, Pair(3, Pair(4, None))))
            )
        self.assertEqual(
            remove(test_list, 2),
            (3, Pair(1, Pair(2, Pair(4, None))))
            )

        with self.assertRaises(IndexError):
            remove(test_list, -1)
        with self.assertRaises(IndexError):
            remove(test_list, 4)


if __name__ == '__main__':
    unittest.main()
