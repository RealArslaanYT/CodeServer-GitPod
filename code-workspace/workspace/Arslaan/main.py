import random

number = random.randint(0, 100)

while True:
    try:
        userNum = int(input("Guess a number: "))
    except ValueError:
        print("That is not a valid number.")
        continue
    
    if userNum == number:
        print(f"You won! The number was {number}!")
        break
    
    if userNum < number:
        print("Too low!")
    
    if userNum > number:
        print("Too high!")