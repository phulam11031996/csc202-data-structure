import unittest

from base_convert import convert


class Tests(unittest.TestCase):
    def test_convert_base02_1(self):
        self.assertEqual(convert(107, 2), '1101011')

    def test_convert_base10_1(self):
        self.assertEqual(convert(107, 10), '107')

    def test_convert_base16_1(self):
        self.assertEqual(convert(107, 16), '6B')

    # TODO: add more tests
    def test_convert_base_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            convert(10, 0)

    def test_convert_base_not_int(self):
        with self.assertRaises(ValueError):
            convert('asd', 1.2)

    def test_convert_base_out_of_bound1(self):
        with self.assertRaises(ValueError):
            convert(10, -4)

    def test_convert_base_out_of_bound2(self):
        with self.assertRaises(ValueError):
            convert(10, 37)


if __name__ == '__main__':
    unittest.main()
