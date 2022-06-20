import unittest

# NOTE: Do not add more imports
from sorts import selection_sort, insertion_sort, merge_sort


class Tests(unittest.TestCase):
    def test_merge_sort_01(self):
        lst = [10]

        # Sorting an singleton list should do no comparisons
        self.assertEqual(merge_sort(lst), 0)

        # The list shouldn't change
        self.assertEqual(lst, [10])

    def test_merge_sort_02(self):
        lst = [50, 60, 10, 20, 80, 40, 30, 70]

        merge_sort(lst)

        # The list should now be sorted
        self.assertEqual(lst, [10, 20, 30, 40, 50, 60, 70, 80])

    # selection_sort()
    def test_selection_sort(self):
        lst_1 = [10]
        lst_2 = [50, 60, 10, 20, 80, 40, 30, 70]
        selection_sort(lst_2)

        self.assertEqual(selection_sort(lst_1), 0)
        self.assertEqual(lst_2, [10, 20, 30, 40, 50, 60, 70, 80])

    # insertion_sort()
    def test_insertion_sort(self):
        lst_1 = [10]
        lst_2 = [50, 60, 10, 20, 80, 40, 30, 70]
        insertion_sort(lst_2)

        self.assertEqual(insertion_sort(lst_1), 0)
        self.assertEqual(lst_2, [10, 20, 30, 40, 50, 60, 70, 80])


if __name__ == '__main__':
    unittest.main()
