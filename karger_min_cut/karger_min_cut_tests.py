import unittest
import karger_min_cut.karger_min_cut as karger

graph = {}
test = {'file': './test-graph.txt', 'nodes': 4.0}


class KargerTests(unittest.TestCase):
	def test_karger(self):
		min_cut = karger.run(test)
		print('minimum cut of %d found' % min_cut)
		self.assertEqual(1, min_cut)
