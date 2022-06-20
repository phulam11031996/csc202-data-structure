import unittest

from array_list import (
    empty_list, add, length, get, setitem, remove)


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

    # empty_list()
    def test_empty(self):
        test_arr = empty_list()
        self.assertEqual(test_arr.list, [None])

    # add()
    def test_add(self):
        test_arr = empty_list()
        add(test_arr, 0, 0)
        add(test_arr, 1, 1)
        add(test_arr, 1, 2)
        add(test_arr, 3, 'a')
        self.assertEqual(test_arr.list, [0, 2, 1, 'a'])
        self.assertEqual(test_arr.size, 4)
        self.assertEqual(test_arr.capacity, 4)
        with self.assertRaises(IndexError):
            add(test_arr, -1, 'error')
        with self.assertRaises(IndexError):
            add(test_arr, 5, 'error')

    # length()
    def test_length(self):
        test_arr = empty_list()
        add(test_arr, 0, 0)
        add(test_arr, 1, 1)
        add(test_arr, 1, 2)
        add(test_arr, 3, 'a')
        self.assertEqual(length(test_arr), 4)

    # get()
    def test_get(self):
        test_arr = empty_list()
        add(test_arr, 0, 0)
        add(test_arr, 1, 1)
        add(test_arr, 1, 2)
        add(test_arr, 3, 'a')
        self.assertEqual(get(test_arr, 0), 0)
        self.assertEqual(get(test_arr, 1), 2)
        self.assertEqual(get(test_arr, 3), 'a')
        with self.assertRaises(IndexError):
            get(test_arr, -1)
        with self.assertRaises(IndexError):
            get(test_arr, 4)

    # setitem()
    def test_setitem(self):
        test_arr = empty_list()
        add(test_arr, 0, 0)
        add(test_arr, 1, 1)
        add(test_arr, 1, 2)
        add(test_arr, 3, 'a')
        setitem(test_arr, 0, 'item')
        self.assertEqual(test_arr.list, ['item', 2, 1, 'a'])
        setitem(test_arr, 3, 'item')
        self.assertEqual(test_arr.list, ['item', 2, 1, 'item'])
        with self.assertRaises(IndexError):
            setitem(test_arr, -1, 'error')
        with self.assertRaises(IndexError):
            setitem(test_arr, 4, 'error')

    # remove()
    def test_remove(self):
        test_arr = empty_list()
        add(test_arr, 0, 0)
        add(test_arr, 1, 1)
        add(test_arr, 1, 2)
        add(test_arr, 3, 'a')
        self.assertEqual(remove(test_arr, 1), (2, [0, 1, 'a', None]))
        self.assertEqual(test_arr.capacity, 4)
        self.assertEqual(test_arr.size, 3)
        with self.assertRaises(IndexError):
            remove(test_arr, -1)
        with self.assertRaises(IndexError):
            remove(test_arr, 3)


if __name__ == '__main__':
    unittest.main()
