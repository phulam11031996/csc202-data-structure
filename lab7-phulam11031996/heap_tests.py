import unittest

from heap import (
    MaxHeap, enqueue, dequeue, peek, size, _contents, heapify, heap_sort)


class Tests(unittest.TestCase):
    def test_heap_simple_operations(self):
        my_heap = MaxHeap()
        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

        enqueue(my_heap, 10)

        self.assertEqual(size(my_heap), 1)
        self.assertEqual(_contents(my_heap), [10])
        self.assertEqual(peek(my_heap), 10)

        self.assertEqual(dequeue(my_heap), 10)

        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

    def test_heapify_simple(self):
        my_heap = heapify([10, 20])
        self.assertEqual(size(my_heap), 2)
        self.assertEqual(_contents(my_heap), [20, 10])

    def test_heap_sort_simple(self):
        my_list = [20, 10]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20])

    # heap_sort()
    def test_heap_sort(self):
        test_list = [1, 6, 3, 8, 7, 0, 3, 8, 4, 6, 3, 6]
        sorted_list = [0, 1, 3, 3, 3, 4, 6, 6, 6, 7, 8, 8]
        heap_sort(test_list)

        self.assertEqual(test_list, sorted_list)

    # peek() and size()
    def test_peek(self):
        heap = MaxHeap()

        self.assertEqual(size(heap), 0)

        with self.assertRaises(IndexError):
            peek(heap)

        with self.assertRaises(IndexError):
            dequeue(heap)

    # enqueue() and dequeue()
    def test_enqueue(self):
        lst_enqueue = [9, 8, 5, 6, 7, 1, 4, 0, 3, 2]
        lst_deqeueu = [4, 3, 1, 0, 2]
        heap = MaxHeap()

        for idx in range(10):
            enqueue(heap, idx)

        self.assertEqual(_contents(heap), lst_enqueue)

        for count in range(5):
            dequeue(heap)

        self.assertEqual(_contents(heap), lst_deqeueu)


if __name__ == '__main__':
    unittest.main()
