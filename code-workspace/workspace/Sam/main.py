import random 
number = random.randint(0,100)
while True:
    usernumber = int(input("guess a number "))
    if usernumber == number:
        print ("you guessed the right number")
        break 