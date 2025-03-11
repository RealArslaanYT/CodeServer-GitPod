import random

number = random.randint(0, 100)

while True:
    userNumber = int(input("Guess a number: "))
    if userNumber == number:
        print("You guessed the right number!")
        break
