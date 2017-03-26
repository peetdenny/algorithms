import unittest
import quicksort.quicksort as sort


class QuicksortTests(unittest.TestCase):
	def test_quicksort(self):
		self.assertEqual([1, 2], sort.sort([2, 1], 0, 1))
		self.assertEqual([1, 2, 3], sort.sort([2, 1, 3], 0, 2))
		self.assertEqual([1000, 2001, 300000], sort.sort([2001, 1000, 300000], 0, 2))
		self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], sort.sort([3, 2, 4, 6, 5, 8, 7, 1], 0, 7))
		self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], sort.sort([3, 2, 4, 9, 10, 11, 6, 5, 12, 8, 7, 1], 0, 11))
