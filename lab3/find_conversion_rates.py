import requests


def query_api(currency_code):
    r = requests.get(f"https://free.currconv.com/api/v7/convert?q={currency_code}_USD&compact=ultra&apiKey"
                     f"=95acd3b1b27702f17001")
    conversion_rate = r.json()[f"{currency_code}_USD"]
    return conversion_rate


class ConversionRates:
    def __init__(self):
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


if __name__ == "__main__":
    print(query_api("RUB"))
