import os,sys
import time
def welcome_call():
    print("\n\t/---------------------------------\\")
    print("\n\t|             Welcome             |")
    print("\n\t|     To The Game Station V 1     |")
    print("\n\t\---------------------------------/")

def game_list():
    print("\n List of games: ")
    print(" 1) Hangman")
    print(" 2) Rock Paper Scissor")
    print(" 3) Find your spirit Animal")
    print(" 4) Burning tree \n")
    print(" 0) Exit")
    optn = input("Enter which game you want to play: ")
    return optn

def game_select(num):
    num  = int(num)
    if num == 1:
        os.system("python hangman.py")
    elif num == 2:
        os.system("python Rock_Paper_Seissor.py")
    elif num == 3:
        os.system("python find_your_spirit_animal.py")
    elif num == 4:
        os.system("python Burning_tree.py")
    else:
        print("Wrong option selected")
        time.sleep(.5)
        

def exit_call():
   string = '\n\n\t\t\tGOOD BYE...'
   for c in string + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.3)

while(1):
    welcome_call()
    num = game_list()
    if num != "" and num != "0":
        game_select(num)
    elif num == "0":
        break 
    else:
        print("You have entered nothing. Try again please")
        time.sleep(1)
    os.system("cls")

os.system("cls")
print("\n\n\n\n\t\t\tYou will be missed... :( ")
exit_call()
time.sleep(0.5)