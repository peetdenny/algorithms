import unittest
import mergesort as sort


class MergeSortTests(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], sort.sort([1, 3, 2, 4, 6, 5, 8, 7, 9]))
