import unittest
import numpy as np
from assn3 import correlation_using_stdlib, read_prices, correlation

appl = read_prices('AAPL')
amzn = read_prices('AMZN')
expected = np.corrcoef(appl, amzn)[0][1]


class MyTestCase(unittest.TestCase):
	def test_correlation_using_stdlib(self):
		self.assertAlmostEqual(expected, correlation_using_stdlib(appl, amzn))

	def test_correlation_using_numpy(self):
		self.assertAlmostEqual(expected, correlation(appl, amzn))


if __name__ == '__main__':
	unittest.main()
