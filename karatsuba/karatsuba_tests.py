import unittest
import karatsuba.karatsuba as karatsuba


class KaratsubaTests(unittest.TestCase):
    def test_basic_multipliers(self):
        self.assertEqual(1200, karatsuba.carrot(20, 60))
        self.assertEqual(7006652, karatsuba.carrot(1234, 5678))
        self.assertEqual(1000000, karatsuba.carrot(1000,1000))

