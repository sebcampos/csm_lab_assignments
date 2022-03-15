# Prologue:
# CIS-117 Lab3
# This activity is about building a module using functions which converts currencies to dollars.
# Group 1, Project 3
# Dillon Anawalt and Sebastian Campos

# GOAL:
# We need 6 functions in total related to conversion, this can be with dollars. To do so, we will convert American
# dollars to Chinese dollars, Mexican dollars, British dollars, Canadian dollars, Russian dollars, Spanish dollars and
# vice-versa!!

# NOTE:
# Dollar value fluctuates over time so for all intents and purposes, we will keep the dollar value the way we
# discovered out of convenience

import Converters

Converter = Converters.Converter()

options = [str(option[0]) for option in enumerate(Converter.conversion_values)]

for number, option in enumerate(Converter.conversion_values):
    print(f"{number} {option}")

user_choice = input("Please select a conversion value: ")

while user_choice not in options:
    user_choice = input("Please select a valid input : ")

chosen_value = int(user_choice)
chosen_amount = float(input("How much money?: "))
if chosen_value == 0:
    conversion, code, symbol = Converter.convert_yuan(chosen_amount)
    print(f'{chosen_amount} in Yuan {symbol}{conversion}')
    conversion, code, symbol = Converter.convert_yuan(chosen_amount, True)
    print(f'{symbol}{chosen_amount} in Dollars {conversion}')
elif chosen_value == 1:
    conversion, code, symbol = Converter.convert_peso(chosen_amount)
    print(f'{chosen_amount} in Peso {symbol}{conversion}')
    conversion, code, symbol = Converter.convert_peso(chosen_amount, True)
    print(f'{symbol}{chosen_amount} in Dollars {conversion}')
elif chosen_value == 2:
    conversion, code, symbol = Converter.convert_pound(chosen_amount)
    print(f'{chosen_amount} in Pound {symbol}{conversion}')
    conversion, code, symbol = Converter.convert_pound(chosen_amount, True)
    print(f'{symbol}{chosen_amount} in Dollars {conversion}')
elif chosen_value == 3:
    conversion, code, symbol = Converter.convert_canadian_dollar(chosen_amount)
    print(f'{chosen_amount} in Canadian Dollar {symbol}{conversion}')
    conversion, code, symbol = Converter.convert_canadian_dollar(chosen_amount, True)
    print(f'{symbol}{chosen_amount} in Dollars {conversion}')

elif chosen_value == 4:
    conversion, code, symbol = Converter.convert_ruble(chosen_amount)
    print(f'{chosen_amount} in Ruble {symbol}{conversion}')
    conversion, code, symbol = Converter.convert_ruble(chosen_amount, True)
    print(f'{symbol}{chosen_amount} in Dollars {conversion}')

elif chosen_value == 5:
    conversion, code, symbol = Converter.convert_euro(chosen_amount)
    print(f'{chosen_amount} in Euro {symbol}{conversion}')
    conversion, code, symbol = Converter.convert_euro(chosen_amount, True)
    print(f'{symbol}{chosen_amount} in Dollars {conversion}')











