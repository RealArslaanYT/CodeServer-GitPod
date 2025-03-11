import random

number = random.randint(0,100)
while True:
    usernumber = int (input("Guess a number: "))
    if usernumber == number:
        print("you gesed the rite number")
        break