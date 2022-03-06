# Chinese dollars, Mexican dollars, British dollars, Canadian dollars, Russian dollars, Spanish dollars

# conversions taken from https://www.xe.com/currencyconverter/convert/
# conversion api https://free.currconv.com/api/v7/

import find_conversion_rates


class Converter:
    def __init__(self) -> None:
        """
        Converter Class initialized with conversion rates saved as attribute conversion values
        Attributes:
          :conversion_values dictionary which
           defines the US dollar amount of 1 unit of the corresponding currency
        """
        self.conversion_values = {
            "Chinese Yuan Renminbi": [0.158252, "¥", "CNY"],
            "Mexican Peso": [0.0477181, "$", "MXN"],
            "British Pound": [1.32300, "£", "GBP"],
            "Canadian Dollar": [0.785367,  "$", "CAD"],
            "Russian Rubles": [0.00816314,  "₽", "RUB"],
            "Spanish Euro": [1.09431, "€", "EUR"]
        }
        self.conversion_rates_api_data = None
        try:
            self.conversion_rates_api_data = find_conversion_rates.ConversionRates().conversion_data
        except Exception as e:
            print("Could Not query API, using hardcoded Values")

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
            conversion = value / self.conversion_values[currency][0]
            return float(f"{conversion:.2f}")
        conversion = value * self.conversion_values[currency][0]
        return float(f"{conversion:.2f}")

    def convert_api(self, currency: str, value: float, reverse: bool = False):
        """
        This method is identical to the convert method but uses the api conversion values instead of the
        hard coded values by referencing the `conversion_rates_api_data`  attribute
        :param currency: currency to be converted as a string
        :param value: value to be converted as a float
        :param reverse: boolean for reverse operation default set to False
        :return: float of conversion representation
        """
        if reverse:
            conversion = value / self.conversion_rates_api_data[currency]["conversion"]
            return float(f"{conversion:.2f}")
        conversion = value * self.conversion_rates_api_data[currency]["conversion"]
        return float(f"{conversion:.2f}")
