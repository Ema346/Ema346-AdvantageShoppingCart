import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdvantageShoppingAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_advantage_shopping():
        methods.setUp()
        methods.teardown()
