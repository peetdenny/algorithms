import unittest
import app.karutsuba as karutsuba

class KarutsubaTests(unittest.TestCase):
    def test_basic_multipliers(self):
        self.assertEqual(1200,karutsuba.carrot(20,60))
        self.assertEqual(1000000,karutsuba.carrot(1000,1000))
        self.assertEqual(7006652,karutsuba.carrot(1234,5678))
