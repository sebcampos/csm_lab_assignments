# CIS-117 Lab3
# This Module tests the Conversion functions in our Converters Module and
# the query_api method from our FindConversionRates module
# Group#
# Dillon Anawalt and Sebastian Campos

import unittest
import Converters
import FindConversionRates

c = Converters.Converter()


class TestUtils(unittest.TestCase):
    """
    This class tests our conversion functions and api query using pythons unittest module
    """
    def test_yuan_conversion(self):
        self.assertEqual(c.convert("Chinese Yuan Renminbi", 15), 2.37)
        print("[PASSED] Chinese Yuan Renminbi 15 equals 2.37")

    def test_peso_conversion(self):
        self.assertEqual(c.convert("Mexican Peso", 43), 2.05)
        print("[PASSED] Mexican Peso 43 equals 2.05")

    def test_pound_conversion(self):
        self.assertEqual(c.convert("British Pound", 79.01), 104.53)
        print("[PASSED] British Pound 79.01 equals 104.53")

    def test_canadian_dollar_conversion(self):
        self.assertEqual(c.convert("Canadian Dollar", 400), 314.15)
        print("[PASSED] Canadian Dollar 400 equals 314.15")

    def test_rubles_conversion(self):
        self.assertEqual(c.convert("Russian Rubles", 7000), 57.14)
        print("[PASSED] Russian Rubles 7000 equals 57.14")

    def test_spanish_euro_conversion(self):
        self.assertEqual(c.convert("Spanish Euro", 19.90), 21.78)
        print("[PASSED] Spanish Euro  19.90 equals 21.78")

    def test_reverse_conversion_yuan(self):
        self.assertEqual(c.convert("Chinese Yuan Renminbi", 15, reverse=True), 94.79)
        print("[PASSED] Chinese Yuan Renminibi 15 reverse operation 94.79")

    def test_api_query(self):
        self.assertEqual(FindConversionRates.query_api("MXN").status_code, 200)
        print("[PASSED] API responded with 200 response code")


if __name__ == '__main__':
    unittest.main()
