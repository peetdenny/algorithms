import unittest
import inversions as inv


class CountInversionsTests(unittest.TestCase):
    def test_inversion_counter(self):
        self.assertEqual(2, inv.count_inversions([1, 2, 3, 5, 4, 6, 7, 8, 9])[1])
        self.assertEqual(4, inv.count_inversions([2, 1, 3, 5, 4, 6, 7, 9, 8])[1])
        #self.assertEqual(1, inv.count_inversions([3, 2, 1, 4, 5, 6, 7, 8, 9])[1])
