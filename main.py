import os

import helper
from helper import calculation_to_minutes, message
from datetime import datetime, timezone
import os
import logging


helper.daysToUnits()
helper.days_to_units(30, "seconds")
# print(9)
# print(f"20 days are {20 * calculation_to_minutes} minutes")
print(f"20 days are {20 * helper.calculation_to_seconds} seconds")

user_input = input("Hi, please can you insert your nick name bellow \n")
try:
    if user_input.isdigit():
        user_input_number = int(user_input)
except ValueError:
    print("Your input is not a valid number!")

print(f"Hi, friend that is your name {user_input}")


def is_number_inserted(number):
    if number > 10:
        print("The project will stopped")


"""
number_input = ""
while number_input != "exit":
    number_input = input("Please insert the number >> ")
    is_number_inserted(int(number_input)) 
"""


# num_of_days_element = 0


def validate_end_executed(num_of_days_element):
    try:
        user_data = int(num_of_days_element)
        if user_data > 0:
            print(f"valid number in hour = {num_of_days_element}")
        elif user_data == 0:
            print("number entered is 0")
        else:
            print("The input is negative")
    except ValueError:
        print("Value entered is not valid number")


"""
number_input = ""
while number_input != "exit":
    number_input = input("Please insert the number or list >> ")
    print(type(number_input))
    print(number_input.split(","))
    for item in number_input.split(", "):
        validate_end_executed(item)
"""
# for number in list_of_numbers:
#     print(number)


# list on python []
list_of_numbers = [1, 3, 6, 9, 99, 3]
# ["one", "two", "four", "three"]

print(list_of_numbers)
print(type(set(list_of_numbers)))
list_of_numbers.append(100)
print(set(list_of_numbers))

my_set = {"Jan", "Feb", "Apr"}
for item in my_set:
    print(item)
my_set.add("May")
print(my_set)

"""
data_input = ""
while data_input != "exit":
    data_input = input("Please insert the number:unit to convert >> ")
    # print(type(number_input))
    days_and_unit = data_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)

"""

# datetime operation
now = datetime.now()
# datetime.datetime(2023, 10, 7, 12, 27, 25, 527961)

# obj.datetime(timezone.utc)

# operation system

print(os.name)

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")

