import unittest
import inversions as inv


class CountInversionsTests(unittest.TestCase):
    def test_inversion_counter(self):
        self.assertEqual(1, inv.count_inversions([1, 2, 3, 5, 4, 6, 7, 8, 9])[1])
        self.assertEqual(3, inv.count_inversions([2, 1, 3, 5, 4, 6, 7, 9, 8])[1])
        self.assertEqual(2, inv.count_inversions([2, 3, 1, 4, 5, 6, 7, 8])[1])
        self.assertEqual(2, inv.count_inversions([11, 1033, 1002, 1000000, 40004])[1])
        self.assertEqual(2, inv.count_inversions([0.011, 1033, 1002, 1000000, 40004])[1])
