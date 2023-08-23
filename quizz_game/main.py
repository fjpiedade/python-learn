print("Wellcome to my Quizz(Computer) Game!")

playing = input("Do you want to play? (yes | no)")
print(playing)
if playing != "yes":
    quit()

print("Okay! Let's Play:) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions Correct!")
