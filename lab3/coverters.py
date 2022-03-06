# Chinese dollars, Mexican dollars, British dollars, Canadian dollars, Russian dollars, Spanish dollars

# conversions taken from https://www.xe.com/currencyconverter/convert/

class Converter:
    def __init__(self) -> None:
        """
        Converter Class initialized with conversion rates saved as attribute coversion values
        Attributes:
          :conversion_values dictionary which
           defines the US dollar amount of 1 unit of the corresponding currency
        """
        self.conversion_values = {
          "Chinese Yuan Renminbi": 0.158252,
          "Mexican Peso": 0.0477181,
          "British Pound": 1.32300,
          "Canadian Dollar": 0.785367,
          "Russian Rubles": 0.00816314,
          "Spanish Euro": 1.09431
        }

    def convert(self, currency: str, value: float, reverse: bool = False) -> float:
        """
        This method performs the conversion of one currency `currency` to american dollars, the conversion
        occurs on the `value` provided then is returned. If the `reverse` bool is set to True then the conversion
        from american dollars to the specified `currency` for the specified `value` is returned
        :param currency: currency to be converted as a string
        :param value: value to be converted as a float
        :param reverse: boolean for reverse operation default set to False
        :return: float of conversion representation
        """
        if reverse:
            conversion = value / self.conversion_values[currency]
            print(f"{value} american dollars equals {currency}:{conversion}")
            return conversion
        conversion = value * self.conversion_values[currency]
        print(f"{currency}:{value} equals {conversion} american dollars")
        return conversion

