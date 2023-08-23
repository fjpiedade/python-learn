import random

# num_random = random.randrange(-1, 11)
# random.randrange(11) # from 0 to 10

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than a 0 on the next time")
        quit()
else:
    print("Please type a number on the next time")
    quit()

num_random = random.randrange(0, top_of_range)
print(num_random)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number on the next time")
        continue

    if user_guess == num_random:
        print("You got it!")
        break
    elif user_guess > num_random:
        print("You are above the number!")
    else:
        print("You are below the number!")

print("You got it in", guesses, "guesses")
