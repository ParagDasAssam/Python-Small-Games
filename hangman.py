import time
import random
import os
os.system("cls")
Movie_list = ["Shrek","Finding Dory","Inside Out","Minions","Brave","Big Hero 6","Wall E","Ratatouille","Toy Story 3","Monsters University","How to Train Your Dragon","The Good Dinosaur"]
Movie_details = {}
def converter(movie):
    Answer = []
    for i in movie:
        if i == " ":
            Answer.append(" ")
        else:
            Answer.append("_")
    return Answer

def printing(Answer):
    print(Movie_list)
    print("\t****************************************")
    print("\t\tWelcome to Hangman..!!")
    print("\t****************************************")
    time.sleep(1)
    print("  The Movie is an animated movie")
    for i in range(len(Answer)):
        if i == 0:
            print("\t",Answer[i],end="")
        else:
            print(Answer[i],end="")

Movie_ = random.choice(Movie_list)
#movie_ = "Shrek hi"
movie = Movie_.lower()

Answer = converter(movie)

#print(Answer)

chances = 3

while("_" in Answer):
    printing(Answer)
    temp = 0
    temp2 = 0
    optn = input("\nEnter your choice: ")
    optn = optn.lower()
    if len(optn) == 1:
        for i in range(len(movie)):
            if movie[i] == optn:
                Answer[i] = optn
                temp = 1
    else:
        if movie.count(optn) != 1:
            temp2 = 1
        if temp2 == 1:
            temp = 0
        else:
            for i in optn:
                for j in range(len(movie)):
                    if movie[j] == i:
                        Answer[j] = i
            temp = 1
                        
    if temp == 0:
        print("Wrong choice..!!")
        chances -= 1
        print("You have",chances,"chances left")
        time.sleep(1)
        if chances == 0:
            time.sleep(1)
            break
        
    os.system("cls")
    
#     break
if chances == 0:
    os.system("cls")
    print("You lost..!!!")
    
else:
    print("The movie was:",Movie_)
    print("You are the winner..!!!")
    time.sleep(2)
exit_ = input("Enter to exit")
