import unittest

from tsort import tsort


class Tests(unittest.TestCase):
    def test_01(self) -> None:
        edges = [['101', '202'], ['202', '203']]
        expected = '101\n202\n203\n'

        self.assertEqual(tsort(edges).strip() + '\n', expected)

    def test_02(self) -> None:
        edges = [
            ['3', '8'], ['3', '10'], ['5', '11'], ['7', '8'], ['7', '11'],
            ['8', '9'], ['11', '2'], ['11', '9'], ['11', '10']
        ]
        expected = '7\n5\n11\n2\n3\n10\n8\n9\n'

        self.assertEqual(tsort(edges).strip() + '\n', expected)

    def test_03(self) -> None:
        edges = [
            ['1', '2'], ['1', '9'], ['1', '8'], ['9', '8'], ['9', '10'],
            ['8', '11'], ['10', '11'], ['2', '3'], ['3', '11'], ['3', '4'],
            ['4', '7'], ['4', '5'], ['7', '5'], ['7', '13'], ['7', '6'],
            ['6', '14'], ['6', '12']
        ]
        expected = '1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11\n'

        self.assertEqual(tsort(edges).strip() + '\n', expected)

    def test_04(self) -> None:
        edges = [['101', '202'], ['202', '203'], ['203', '202']]
        with self.assertRaises(ValueError):
            tsort(edges)


if __name__ == '__main__':
    unittest.main()
