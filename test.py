import unittest
import numpy as np
from assn3 import correlation_using_stdlib, read_prices, correlation_using_numpy


class MyTestCase(unittest.TestCase):
	def test_correlation_using_stdlib(self):
		self.assertAlmostEqual(
			0.8405047735028569,
			correlation_using_stdlib(read_prices('AAPL'), read_prices('AMZN')),
		)

	def test_correlation_using_numpy(self):
		self.assertAlmostEqual(
			0.8405047735028567,
			correlation_using_numpy(np.array(read_prices('AAPL')), np.array(read_prices('AMZN'))),
		)


if __name__ == '__main__':
	unittest.main()
