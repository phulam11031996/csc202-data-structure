import unittest

from ordered_list import (
    OrderedList, insert, remove, contains, index, get, pop, is_empty, size)


class Tests(unittest.TestCase):
    def test_simple(self) -> None:
        my_list = OrderedList()

        insert(my_list, 10)

        self.assertEqual(size(my_list), 1)
        self.assertTrue(contains(my_list, 10))
        self.assertFalse(is_empty(my_list))
        self.assertEqual(index(my_list, 10), 0)
        self.assertEqual(get(my_list, 0), 10)

        remove(my_list, 10)

        self.assertEqual(size(my_list), 0)
        self.assertFalse(contains(my_list, 10))
        self.assertTrue(is_empty(my_list))

        insert(my_list, 10)

        self.assertEqual(pop(my_list, 0), 10)
        self.assertEqual(size(my_list), 0)
        self.assertFalse(contains(my_list, 10))
        self.assertTrue(is_empty(my_list))

    def test_some_more(self):
        my_list = OrderedList()

        insert(my_list, 50)
        insert(my_list, 40)
        insert(my_list, 30)
        insert(my_list, 20)
        insert(my_list, 10)
        remove(my_list, 10)
        remove(my_list, 50)
        remove(my_list, 30)

        # tests remove()
        with self.assertRaises(ValueError):
            remove(my_list, 0)

        # tests contains()
        self.assertFalse(contains(my_list, 50))
        self.assertTrue(contains(my_list, 20))

        # tests index()
        with self.assertRaises(ValueError):
            index(my_list, 50)
        self.assertEqual(index(my_list, 20), 0)

        # tests get()
        with self.assertRaises(IndexError):
            get(my_list, -1)
        self.assertEqual(get(my_list, 0), 20)

        # tests pop()
        insert(my_list, 0)
        insert(my_list, 100)
        insert(my_list, 90)
        with self.assertRaises(IndexError):
            pop(my_list, 50)
        self.assertEqual(pop(my_list, 0), 0)
        self.assertEqual(pop(my_list, 3), 100)

        # tests is_empty()
        self.assertFalse(is_empty(my_list))

        # tests size()
        self.assertEqual(size(my_list), 3)


if __name__ == '__main__':
    unittest.main()
