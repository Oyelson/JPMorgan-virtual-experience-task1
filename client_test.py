import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # check if we have accurate positioning and correct data point 
      # and the price is correctly calculated.
      bid_price = quote["top_bid"]["price"]
      ask_price = quote["top_ask"]["price"]
      price = (bid_price + ask_price) / 2.0
      accurate_dataPoint = (quote["stock"], bid_price, ask_price, price)
      self.assertEqual(getDataPoint(quote), accurate_dataPoint)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      # check if we have accurate positioning and correct data point 
      # and the price is correctly calculated.
      bid_price = quote["top_bid"]["price"]
      ask_price = quote["top_ask"]["price"]
      price = (bid_price + ask_price) / 2.0
      accurate_dataPoint = (quote["stock"], bid_price, ask_price, price)
      self.assertEqual(getDataPoint(quote), accurate_dataPoint)


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_isOf_validLength(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    # check if we have complete data point (4 values in this case).
    for quote in quotes:
      self.assertEqual(len(getDataPoint(quote)), 4)
  
  def test_getRatio_priceBIsZero(self):
    price_a = 121.68
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))
  
  def test_getRatio_priceAIsZero(self):
    price_a = 0
    price_b = 121.68
    self.assertEqual(getRatio(price_a, price_b), 0)
  
  def test_getRatio_greaterThan1(self):
    price_a = 121.68
    price_b = 119.68
    self.assertGreater(getRatio(price_a, price_b), 1)

  def test_getRatio_lessThan1(self):
    price_a = 119.68
    price_b = 121.68
    self.assertLess(getRatio(price_a, price_b), 1)

  def test_getRatio_exactlyOne(self):
    price_a = 121.68
    price_b = 121.68
    self.assertEqual(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
