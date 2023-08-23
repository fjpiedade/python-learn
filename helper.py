calculation_to_seconds = 24 * 60 * 60
calculation_to_minutes = 24 * 60

message = "My Litter Life"


def daysToUnits():
    print(f"20 days are {20 * calculation_to_minutes} minutes")
    print("endOfFunction")


def days_to_units(num_of_days, name_of_unit):
    calc = 0
    if name_of_unit == "seconds":
        calc = 24 * 60 * 60
    if name_of_unit == "minutes":
        calc = 24 * 60
    print(f"{num_of_days} days are {num_of_days * calc} {name_of_unit}")


def is_number_inserted(number):
    if number > 10:
        print("The project will stopped")


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
