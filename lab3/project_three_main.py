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

user_choice = int(input("Please select a conversion value: "))

while user_choice not in options:
    user_choice = int(input("Please select a valid input : "))

chosen_value = int(user_choice)

if chosen_value == _ :







