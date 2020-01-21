import random,os
min = 1
max = 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    os.system("cls")
    print ("Rolling the dice............")
    print ("The value is..............")
    print (random.randint(min, max))
    roll_again = input("Enter y to roll the dice again? ")

input("Press<enter> to exit")
