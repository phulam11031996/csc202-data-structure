import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    # TODO: add more tests
    def test_bears_value_error(self):
        with self.assertRaises(ValueError):
            bears('asd')

    def test_bears_out_of_bound(self):
        with self.assertRaises(ValueError):
            bears(-1)

    def test_bears_1(self):
        self.assertTrue(bears(250))

    def test_bears_2(self):
        self.assertFalse(bears(251))

    def test_bears_3(self):
        self.assertTrue(bears(255))

    def test_bears_4(self):
        self.assertFalse(bears(60))


if __name__ == '__main__':
    unittest.main()
