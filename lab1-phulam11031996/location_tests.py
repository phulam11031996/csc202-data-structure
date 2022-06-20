import unittest

from location import Location


class Tests(unittest.TestCase):
    def test_location_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")


if __name__ == '__main__':
    unittest.main()
