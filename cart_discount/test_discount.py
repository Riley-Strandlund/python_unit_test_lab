import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

    # test with a list of 2 prices
    def test_list_of_two_prices(self):
        prices = [2, 20]
        self.assertIsNone(discount(prices))
    # test with a list 1 price 
    def test_list_of_one_price(self):
        prices = [2.32]
        self.assertIsNone(discount(prices))
    # a list of 6 prices?
    def test_list_of_six_prices(self):
        prices = [2.23, 1, 15, 999, 43, 10]
        expected_discount = 1
        self.assertEqual(expected_discount, discount(prices))
    # what other data might this function have to deal with?
    def test_list_of_strings(self):
        prices = ['1','2','87']
        # TODO what -do- we expect?
        # input into webforms is usually a string, as opoosed to int or float.
    def if_empty(self):
        prices = []
        self.fail(discount(prices))
    # remember a function has no control over how it is used
    # it may be called with any data - and it should be able to handle whatever data it gets appropriatly.

if __name__ == '__main__':
    unittest.main()