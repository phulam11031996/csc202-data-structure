import unittest

from bst import (
    TreeNode, prefix_iterator, infix_iterator, postfix_iterator)


class Tests(unittest.TestCase):
    def test_sample(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        infix_iter = infix_iterator(tree)
        expected = [1, 2, 3, 4, 5, 6, 7]

        for value in expected:
            self.assertEqual(next(infix_iter), value)

        with self.assertRaises(StopIteration):
            next(infix_iter)

    # test all iterators
    def test_iterators(self):
        test_tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        prefix = [4, 2, 1, 3, 6, 5, 7]
        infix = [1, 2, 3, 4, 5, 6, 7]
        postfix = [1, 3, 2, 5, 7, 6, 4]

        for idx, iter in zip(range(len(prefix)), prefix_iterator(test_tree)):
            self.assertEqual(iter, prefix[idx])

        for idx, iter in zip(range(len(prefix)), infix_iterator(test_tree)):
            self.assertEqual(iter, infix[idx])

        for idx, iter in zip(range(len(postfix)), postfix_iterator(test_tree)):
            self.assertEqual(iter, postfix[idx])


if __name__ == '__main__':
    unittest.main()
