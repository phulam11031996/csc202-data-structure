import unittest

from linked_queue import (
    empty_queue, enqueue, dequeue, peek, is_empty, size)


class Tests(unittest.TestCase):
    # is_empty
    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    # empty_queue
    def test_empty_queue(self):
        test_queue = empty_queue()
        self.assertEqual(test_queue.head, None)
        self.assertEqual(test_queue.tail, None)

    # enqueue and dequeue
    def test_enqueue_dequeue(self):
        test_queue = empty_queue()
        with self.assertRaises(IndexError):
            dequeue(test_queue)

        enqueue(test_queue, 'a')
        enqueue(test_queue, 'b')
        enqueue(test_queue, 'c')
        self.assertEqual(test_queue.head.value, 'a')
        self.assertEqual(test_queue.tail.value, 'c')
        self.assertEqual(test_queue.size, 3)

        self.assertEqual(dequeue(test_queue), 'a')
        self.assertEqual(test_queue.head.value, 'b')
        self.assertEqual(test_queue.tail.value, 'c')
        self.assertEqual(test_queue.size, 2)

    # peek
    def test_peek(self):
        test_queue = empty_queue()
        with self.assertRaises(IndexError):
            peek(test_queue)

        enqueue(test_queue, 'a')
        enqueue(test_queue, 'b')
        enqueue(test_queue, 'c')
        self.assertEqual(peek(test_queue), 'a')
        self.assertEqual(test_queue.tail.value, 'c')

    # size
    def test_size(self):
        test_queue = empty_queue()
        self.assertEqual(size(test_queue), 0)

        enqueue(test_queue, 'a')
        dequeue(test_queue)
        enqueue(test_queue, 'c')
        self.assertEqual(size(test_queue), 1)


if __name__ == '__main__':
    unittest.main()
