import requests


def query_api(currency_code: str) -> requests.Response:
    """
    This method takes in a valid currency code as a string and queries an api for the value of
    :param currency_code: str representation of currency code
    :return: Response object
    """
    r = requests.get(f"https://free.currconv.com/api/v7/convert?q={currency_code}_USD&compact=ultra&apiKey"
                     f"=95acd3b1b27702f17001")
    return r


def parse_api_response(r: requests.Response) -> float:
    """
    This method takes in the Response object and extracts the conversion value
    :param r: Response object from the `query_api` method
    :return: conversion rate as a float
    """
    conversion_rate = list(r.json().values())[0]
    return conversion_rate


class ConversionRates:
    def __init__(self) -> None:
        """
        class ConversionRates:
            This class has the hardcoded names, symbols and currency codes as a python dictionary
            saved in the conversion_data attribute. On init the method queries an API using each item's `code`
            value. The API returns the conversion rate and then it is saved into the dictionary as the key `conversion`
        Attributes:
            :conversion_data a python dictionary holding conversion data
        """
        self.conversion_data = {
            "Chinese Yuan Renminbi":
                {
                    "symbol": "¥",
                    "code": "CNY"
                },
            "Mexican Peso":
                {
                    "symbol": "$",
                    "code": "MXN"
                },
            "British Pound":
                {
                    "symbol": "£",
                    "code": "GBP"
                },
            "Canadian Dollar":
                {
                    "symbol": "$",
                    "code": "CAD"
                },
            "Russian Rubles":
                {
                    "symbol": "₽",
                    "code": "RUB"
                },
            "Spanish Euro":
                {
                    "symbol": "€",
                    "code": "EUR"
                }
        }
        for key in self.conversion_data:
            code = self.conversion_data[key]["code"]
            api_response = query_api(code)
            conversion = parse_api_response(api_response)
            self.conversion_data[key]["conversion"] = conversion

