import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Dear user! Time remaining for your goal: {goal} is {time_till.days} days")

# print(input_list)
