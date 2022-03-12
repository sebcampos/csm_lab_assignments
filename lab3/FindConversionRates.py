# CIS-117 Lab3
# This Module Contains the ConversionRates class and related functions which
# query the free.currconv api to collect and save conversion rates as an
# attribute of the class
# Group 1, Project 3
# Dillon Anawalt and Sebastian Campos

import requests
from requests import Response


def query_api(currency_code: str) -> Response:
    """
    This method takes in a valid currency code as a string and queries an api for the value of
    :param currency_code: str representation of currency code
    :return: Response object
    """
    r = requests.get(f"https://free.currconv.com/api/v7/convert?q={currency_code}_USD&compact=ultra&apiKey"
                     f"=95acd3b1b27702f17001")
    return r


def parse_api_response(r: Response) -> float:
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
            This class contains names, currency symbols, and currency codes as an attribute
            called conversion_data . On init the method queries an API for each value to collect the conversion
            amount
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
        print("Using API provided Conversion Rates")
