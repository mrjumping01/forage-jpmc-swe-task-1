import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
	def test_getDataPoint_calculatePrice(self):
		quotes = [
			{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		""" ------------ Add the assertion below ------------ """
		for quote in quotes:
			self.assertTupleEqual(getDataPoint(quote), ( quote["stock"], quote["top_ask"]["price"], quote["top_bid"]["price"], 0.5 * (quote["top_bid"]["price"] + quote["top_ask"]["price"]) ))


	def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
		quotes = [
			{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		""" ------------ Add the assertion below ------------ """
		for quote in quotes:
			self.assertTupleEqual(getDataPoint(quote), ( quote["stock"], quote["top_ask"]["price"], quote["top_bid"]["price"], 0.5 * (quote["top_bid"]["price"] + quote["top_ask"]["price"]) ))


	""" ------------ Add more unit tests ------------ """
	def test_getDataPoint_calculatePriceBidLessThan_Ask(self):
		quotes = [
			{'top_ask': {'price': 145.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
			{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		for quote in quotes:
			self.assertTupleEqual(getDataPoint(quote), ( quote["stock"], quote["top_ask"]["price"], quote["top_bid"]["price"], 0.5 * (quote["top_bid"]["price"] + quote["top_ask"]["price"]) ))

	def test_getRatio_calculateRatio(self):
		a, b = 145.2, 256.9
		self.assertEqual(getRatio(a, b), a / b)

	def test_getRatio_zeroDenominatorReturnsNull(self):
		a, b = 145.2, 0
		self.assertIsInstance(getRatio(a, b), None, "Denominator is zero")




if __name__ == '__main__':
	unittest.main()
