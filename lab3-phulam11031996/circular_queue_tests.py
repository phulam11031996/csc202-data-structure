import unittest

from circular_queue import (
    empty_queue, enqueue, dequeue, peek, is_empty, size)


class Tests(unittest.TestCase):
    # is_empty
    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    # enqueue, dequeue, peek, size
    def test_enqueue_and_dequeue(self):
        test_queue = empty_queue()
        with self.assertRaises(IndexError):     # test IndexError dequeue
            dequeue(test_queue)
        with self.assertRaises(IndexError):     # test IndexError peek
            peek(test_queue)

        for i in range(8):                      # do some enqueues
            enqueue(test_queue, i)

        for i in range(3):                      # do some dequeues
            dequeue(test_queue)

        for i in range(4):                      # do some enqueues
            enqueue(test_queue, i)

        for i in range(7):                      # do some dequeues
            dequeue(test_queue)

        self.assertEqual(dequeue(test_queue), 2)    # test dequeue's return ele
        self.assertEqual(size(test_queue), 1)       # test size
        self.assertEqual(test_queue.head, 1)        # test head
        self.assertEqual(peek(test_queue), 3)       # test peek
        self.assertEqual(test_queue.capacity, 10)   # test capacity
        self.assertEqual(                           # test circullar queue
            test_queue.cir_queue,
            [None, 3, None, None, None, None, None, None, None, None]
            )


if __name__ == '__main__':
    unittest.main()
