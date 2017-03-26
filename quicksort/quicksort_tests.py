import unittest
import quicksort.quicksort as sort


class QuicksortTests(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual([1, 2], sort.sort([2, 1], 0, 1))
        self.assertEqual([1, 2, 3], sort.sort([2, 1, 3], 0, 2))
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], sort.sort([3, 2, 4, 6, 5, 8, 7, 1], 0, 7))
