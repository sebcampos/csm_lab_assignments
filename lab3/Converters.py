# CIS-117 Lab3
# This module contains the Converter class which provides functions to convert currency from USD to
# CNY, MXN, GBP, CAD, RUB, and EUR
# Group 1, Project 3
# Dillon Anawalt and Sebastian Campos

# conversions taken from https://www.xe.com/currencyconverter/convert/
# conversion api https://free.currconv.com/api/v7/

import os


class Converter:
    def __init__(self, test=False) -> None:
        """
        Converter Class initialized with conversion rates saved as attribute conversion values
        Attributes:
          :conversion_values dictionary which
           defines the US dollar amount of 1 unit of the corresponding currency
        :return: None
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
        if not test:
            try:
                import FindConversionRates
                self.conversion_values = FindConversionRates.ConversionRates().conversion_data
            except:
                pass

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

    def convert_yuan(self, value: float, reverse=False) -> tuple:
        conversion = self.convert("Chinese Yuan Renminbi", value, reverse)
        code = self.conversion_values["Chinese Yuan Renminbi"]["code"]
        symbol = self.conversion_values["Chinese Yuan Renminbi"]["symbol"]
        return conversion, code, symbol

    def convert_peso(self, value: float, reverse=False) -> tuple:
        conversion = self.convert("Mexican Peso", value, reverse)
        code = self.conversion_values["Mexican Peso"]["code"]
        symbol = self.conversion_values["Mexican Peso"]["symbol"]
        return conversion, code, symbol

    def convert_ruble(self, value: float, reverse=False) -> tuple:
        conversion = self.convert("Russian Rubles", value, reverse)
        code = self.conversion_values["Russian Rubles"]["code"]
        symbol = self.conversion_values["Russian Rubles"]["symbol"]
        return conversion, code, symbol

    def convert_euro(self, value: float, reverse=False) -> tuple:
        conversion = self.convert("Spanish Euro", value, reverse)
        code = self.conversion_values["Spanish Euro"]["code"]
        symbol = self.conversion_values["Spanish Euro"]["symbol"]
        return conversion, code, symbol

    def convert_pound(self, value: float, reverse=False) -> tuple:
        conversion = self.convert("British Pound", value, reverse)
        code = self.conversion_values["British Pound"]["code"]
        symbol = self.conversion_values["British Pound"]["symbol"]
        return conversion, code, symbol

    def convert_canadian_dollar(self, value: float, reverse=False) -> tuple:
        conversion = self.convert("Canadian Dollar", value, reverse)
        code = self.conversion_values["Canadian Dollar"]["code"]
        symbol = self.conversion_values["Canadian Dollar"]["symbol"]
        return conversion, code, symbol


if __name__ == "__main__":  # if run as top module, will run testing suite with converter arg test set to True.
    print("[Testing Conversion Methods]\n\n")
    os.system("python TestConversions.py")
