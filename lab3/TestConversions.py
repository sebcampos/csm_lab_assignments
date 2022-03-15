# CIS-117 Lab3
# This Module tests the Conversion functions in our Converters Module and
# the query_api method from our FindConversionRates module
# Group#
# Dillon Anawalt and Sebastian Campos

import unittest
import Converters
from FindConversionRates import query_api
import sys
import logging

c = Converters.Converter(test=True)


class ConversionTests(unittest.TestCase):
    """
    This class tests our conversion functions and api query using pythons unittest module
    """

    def test_yuan_conversion(self):
        log = logging.getLogger("ConversionTests.test_yuan_conversion")
        self.assertEqual(c.convert_yuan(15)[0], 2.37)
        log.debug(" [PASSED] 15 equals 2.37")

    def test_peso_conversion(self):
        log = logging.getLogger("ConversionTests.test_peso_conversion")
        self.assertEqual(c.convert_peso(43)[0], 2.05)
        log.debug(" [PASSED] 43 equals 2.05")

    def test_pound_conversion(self):
        log = logging.getLogger("ConversionTests.test_pound_conversion")
        self.assertEqual(c.convert_pound(79.01)[0], 104.53)
        log.debug(" [PASSED] 79.01 equals 104.53")

    def test_canadian_dollar_conversion(self):
        log = logging.getLogger("ConversionTests.test_canadian_dollar_conversion")
        self.assertEqual(c.convert_canadian_dollar(400)[0], 314.15)
        log.debug(" [PASSED] 400 equals 314.15")

    def test_rubles_conversion(self):
        log = logging.getLogger("ConversionTests.test_rubles_conversion")
        self.assertEqual(c.convert_ruble(7000)[0], 57.14)
        log.debug(" [PASSED] 7000 equals 57.14")

    def test_spanish_euro_conversion(self):
        log = logging.getLogger("ConversionTests.test_spanish_euro_conversion")
        self.assertEqual(c.convert_euro(19.90)[0], 21.78)
        log.debug(" [PASSED] 19.90 equals 21.78")

    def test_reverse_conversion_yuan(self):
        log = logging.getLogger("ConversionTests.test_reverse_conversion_yuan")
        self.assertEqual(c.convert_yuan(15, reverse=True)[0], 94.79)
        log.debug(" [PASSED] 15 equals 94.79")

    def test_api_query(self):
        log = logging.getLogger("ConversionTests.test_api_query")
        self.assertEqual(query_api("MXN").status_code, 200)
        log.debug(" [PASSED] API returned 200 response code")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("ConversionTests.test_yuan_conversion").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_peso_conversion").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_pound_conversion").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_canadian_dollar_conversion").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_rubles_conversion").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_spanish_euro_conversion").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_reverse_conversion_yuan").setLevel(logging.DEBUG)
    logging.getLogger("ConversionTests.test_api_query").setLevel(logging.DEBUG)
    unittest.main()
