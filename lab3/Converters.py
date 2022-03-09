# CIS-117 Lab3
# This module contains the Converter class which provides functions to convert currency from USD to
# CNY, MXN, GBP, CAD, RUB, and EUR
# Group 1, Project 3
# Dillon Anawalt and Sebastian Campos

# conversions taken from https://www.xe.com/currencyconverter/convert/
# conversion api https://free.currconv.com/api/v7/
import FindConversionRates
from json.decoder import JSONDecodeError


class Converter:
    def __init__(self) -> None:
        """
        Converter Class initialized with conversion rates saved as attribute conversion values
        Attributes:
          :conversion_values dictionary which
           defines the US dollar amount of 1 unit of the corresponding currency
        """
        self.conversion_values = {
            "Chinese Yuan Renminbi":
                {
                    "conversion": 0.158252,
                    "symbol": "¥",
                    "code": "CNY"
                },
            "Mexican Peso":
                {
                    "conversion": 0.0477181,
                    "symbol": "$",
                    "code": "MXN"
                },
            "British Pound":
                {
                    "conversion": 1.32300,
                    "symbol": "£",
                    "code": "GBP"
                },
            "Canadian Dollar":
                {
                    "conversion": 0.785367,
                    "symbol": "$",
                    "code": "CAD"
                },
            "Russian Rubles":
                {
                    "conversion": 0.00816314,
                    "symbol": "₽",
                    "code": "RUB"
                },
            "Spanish Euro":
                {
                    "conversion": 1.09431,
                    "symbol": "€",
                    "code": "EUR"
                }
        }
        try:
            self.conversion_values = FindConversionRates.ConversionRates().conversion_data
        except JSONDecodeError:
            print("[SERVER UNAVAILABLE] Could Not query API, using hardcoded Values")

    def convert(self, currency: str, value: float, reverse: bool = False) -> float:
        """
        This method uses `currency` to find the american dollar value in the `conversion_values` attribute
        Then it multiplies the provided `value` argument by the located conversion. If the `reverse` arguement is
        set to True then the reverse operation is returned
        :param currency: currency to be converted as a string
        :param value: value to be converted as a float
        :param reverse: boolean for reverse operation default set to False
        :return: float of conversion representation
        """
        if reverse:
            conversion = value / self.conversion_values[currency]["conversion"]
            return float(f"{conversion:.2f}")
        conversion = value * self.conversion_values[currency]["conversion"]
        return float(f"{conversion:.2f}")


if __name__ == "__main__":
    print("Testing Conversion Methods")
    with open("TestConversions.py", "r") as f:
        string = f.read()
    exec(string)
