# CIS-117 Lab3
# This Module tests the Conversion functions in our Converters Module and
# the query_api method from our FindConversionRates module
# Group#
# Dillon Anawalt and Sebastian Campos

import unittest
import Converters
import FindConversionRates
import sys
import logging

c = Converters.Converter()


class ConversionTests(unittest.TestCase):
    """
    This class tests our conversion functions and api query using pythons unittest module
    """

    def test_yuan_conversion(self):
        log = logging.getLogger("ConversionTests.test_yuan_conversion")
        self.assertEqual(c.convert("Chinese Yuan Renminbi", 15), 2.37)
        log.debug(" [PASSED] 15 equals 2.37")

    def test_peso_conversion(self):
        log = logging.getLogger("ConversionTests.test_peso_conversion")
        self.assertEqual(c.convert("Mexican Peso", 43), 2.05)
        log.debug(" [PASSED] 43 equals 2.05")

    def test_pound_conversion(self):
        log = logging.getLogger("ConversionTests.test_pound_conversion")
        self.assertEqual(c.convert("British Pound", 79.01), 104.53)
        log.debug(" [PASSED] 79.01 equals 104.53")

    def test_canadian_dollar_conversion(self):
        log = logging.getLogger("ConversionTests.test_canadian_dollar_conversion")
        self.assertEqual(c.convert("Canadian Dollar", 400), 314.15)
        log.debug(" [PASSED] 400 equals 314.15")

    def test_rubles_conversion(self):
        log = logging.getLogger("ConversionTests.test_rubles_conversion")
        self.assertEqual(c.convert("Russian Rubles", 7000), 57.14)
        log.debug(" [PASSED] 7000 equals 57.14")

    def test_spanish_euro_conversion(self):
        log = logging.getLogger("ConversionTests.test_spanish_euro_conversion")
        self.assertEqual(c.convert("Spanish Euro", 19.90), 21.78)
        log.debug(" [PASSED] 19.90 equals 21.78")

    def test_reverse_conversion_yuan(self):
        log = logging.getLogger("ConversionTests.test_reverse_conversion_yuan")
        self.assertEqual(c.convert("Chinese Yuan Renminbi", 15, reverse=True), 94.79)
        log.debug(" [PASSED] 15 equals 94.79")

    def test_api_query(self):
        log = logging.getLogger("ConversionTests.test_canadian_dollar_conversion")
        self.assertEqual(FindConversionRates.query_api("MXN").status_code, 200,
                         "[FAILED] API did not respond with 200 response code")
        log.debug("[PASSED] Request to API responded with 200 response code")


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
