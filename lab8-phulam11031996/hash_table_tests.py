import unittest

from hash_table import (
    HashTable, insert, get_item, contains, remove, size, keys, load_factor,
    _contents)


def bad_hash(val) -> int:
    return 0


class Tests(unittest.TestCase):
    def test_hash_table_empty(self) -> None:
        ht = HashTable(1)

        self.assertEqual(size(ht), 0)
        self.assertAlmostEqual(load_factor(ht), 0.0)
        self.assertFalse(contains(ht, 0))
        self.assertEqual(keys(ht), [])
        self.assertEqual(_contents(ht), [[]])

    def test_hash_table_insert(self) -> None:
        ht = HashTable(1)
        insert(ht, 0, 'cat')

        self.assertEqual(get_item(ht, 0), 'cat')
        self.assertEqual(size(ht), 1)
        self.assertAlmostEqual(load_factor(ht), 1.0)
        self.assertTrue(contains(ht, 0))
        self.assertEqual(keys(ht), [0])
        self.assertEqual(_contents(ht), [[(0, 'cat')]])

        # re-insert the same key
        insert(ht, 0, 'dog')

        self.assertEqual(get_item(ht, 0), 'dog')
        self.assertEqual(size(ht), 1)
        self.assertAlmostEqual(load_factor(ht), 1.0)
        self.assertTrue(contains(ht, 0))
        self.assertEqual(keys(ht), [0])
        self.assertEqual(_contents(ht), [[(0, 'dog')]])

    def test_hash_table_remove(self) -> None:
        ht = HashTable(1)
        insert(ht, 0, 'cat')

        self.assertEqual(remove(ht, 0), (0, 'cat'))

        self.assertEqual(size(ht), 0)
        self.assertAlmostEqual(load_factor(ht), 0.0)
        self.assertFalse(contains(ht, 0))
        self.assertEqual(keys(ht), [])
        self.assertEqual(_contents(ht), [[]])

        with self.assertRaises(KeyError):
            get_item(ht, 0)

    def test_hash_table_double_capacity(self) -> None:
        ht = HashTable(1)

        insert(ht, 7, 'cat')
        insert(ht, 2, 'dog')

        self.assertEqual(_contents(ht), [[(2, 'dog')], [(7, 'cat')]])

        insert(ht, 4, 'snake')

        self.assertEqual(
            _contents(ht),
            [[(4, 'snake')], [], [(2, 'dog')], [(7, 'cat')]])

    def test_hash_table_bad_hash_function(self) -> None:
        # Use a custom hashing function for the keys
        ht = HashTable(10, bad_hash)

        for i in range(10):
            insert(ht, 'key %d' % i, i)
        # All the keys are inserted into the chain at index 0
        self.assertEqual(
            _contents(ht),
            [[('key 0', 0), ('key 1', 1), ('key 2', 2), ('key 3', 3),
              ('key 4', 4), ('key 5', 5), ('key 6', 6), ('key 7', 7),
              ('key 8', 8), ('key 9', 9)],
             [], [], [], [], [], [], [], [], []])

    # my tests
    def test_for_error(self):
        ht = HashTable()
        insert(ht, 0, 'cat')
        insert(ht, 1, 'dog')
        insert(ht, 3, 'mouse')

        with self.assertRaises(KeyError):
            get_item(ht, 4)
        with self.assertRaises(KeyError):
            remove(ht, 4)

    # do all test
    def test_all(self):
        ht = HashTable()

        for idx in range(10):
            insert(ht, idx, 'cat ' + str(idx))

        self.assertEqual(get_item(ht, 5), 'cat 5')
        self.assertTrue(contains(ht, 4))
        self.assertFalse(contains(ht, 10))
        self.assertEqual(remove(ht, 1), (1, 'cat 1'))
        self.assertEqual(size(ht), 9)
        self.assertEqual(keys(ht), [0, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertAlmostEqual(load_factor(ht), 9.0/10.0)


if __name__ == '__main__':
    unittest.main()
