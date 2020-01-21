import os,sys
import time
def welcome_call():
    print("\n\t/---------------------------------\\")
    print("\n\t|                                 |")
    print("\n\t|        Game Station V 1         |")
    print("\n\t|                                 |")
    print("\n\t\---------------------------------/")

def game_list():
    print("\n List of games: ")
    print(" 1) Hangman")
    print(" 2) Rock Paper Scissor")
    print(" 3) Find your spirit Animal")
    print(" 4) Burning tree")
    print(" 5) hangman 2.0")
    print(" 6) Guess the number")
    print(" 0) Exit")
    optn = input("\nEnter which game you want to play: ")
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
    elif num == 5:
        os.system("python hangman_2.0.py")
    elif num == 6:
        os.system("python guess_my_number.py")
    else:
        print("Wrong option selected")
        time.sleep(.5)
        

def exit_call():
   string = '\n\n\t\t\tGOOD BYE...'
   for c in string + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.2)

def Entry_call():
    string = '\n\n\n\t\tWelcome to Game Station V 1   '
    for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)
    time.sleep(.2)
    

Entry_call()
os.system("cls")
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