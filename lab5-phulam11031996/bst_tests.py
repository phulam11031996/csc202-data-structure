import unittest

from bst import (
    is_empty, search, insert, delete, find_min, find_max, height, TreeNode)


class Tests(unittest.TestCase):
    def test_sample(self):
        tree = None

        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        self.assertFalse(search(tree, 10))
        self.assertEqual(delete(tree, 10), tree)

        tree = insert(tree, 10)

        self.assertTrue(search(tree, 10))
        self.assertEqual(find_min(tree), 10)
        self.assertEqual(find_max(tree), 10)

    # is_empty()
    def test_is_empty(self):
        test_tree = None
        self.assertTrue(is_empty(test_tree))

        test_tree = insert(test_tree, 10)
        self.assertFalse(is_empty(test_tree))

    # search()
    def test_search(self):
        test_tree = TreeNode(
                12,
                TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
                TreeNode(18, TreeNode(14, None, TreeNode(16)), TreeNode(23)))
        self.assertTrue(search(test_tree, 16))
        self.assertFalse(search(test_tree, 0))

    # insert()
    def test_insert(self):
        test_tree = TreeNode(12)
        test_tree = insert(test_tree, 7)
        test_tree = insert(test_tree, 18)
        test_tree = insert(test_tree, 2)
        test_tree = insert(test_tree, 10)
        test_tree = insert(test_tree, 14)
        test_tree = insert(test_tree, 23)
        tree_eq = TreeNode(
            12,
            TreeNode(7, TreeNode(2), TreeNode(10)),
            TreeNode(18, TreeNode(14), TreeNode(23))
            )
        self.assertEqual(test_tree, tree_eq)

    # delete()
    def test_delete_all(self):
        tree = None

        for val in [50, 40, 20, 30, 60, 10, 80, 70]:
            tree = insert(tree, val)

        for val in [50, 10, 20, 30, 40, 60, 70, 80]:
            tree = delete(tree, val)

        self.assertIsNone(tree)

    # find_min(), find_max()), height()
    def test_find_max_find_min_height(self):
        test_tree = TreeNode(
                12,
                TreeNode(7, TreeNode(2), TreeNode(10, TreeNode(9), None)),
                TreeNode(18, TreeNode(14, None, TreeNode(16)), TreeNode(23)))
        test_tree_none = None

        self.assertEqual(find_max(test_tree), 23)
        with self.assertRaises(ValueError):
            find_max(test_tree_none)
        with self.assertRaises(ValueError):
            find_min(test_tree_none)
        self.assertEqual(find_min(test_tree), 2)
        self.assertEqual(height(test_tree), 3)
        self.assertEqual(height(test_tree_none), -1)
        delete(test_tree, 14)   # test coverage


if __name__ == '__main__':
    unittest.main()
