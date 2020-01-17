import os,sys
import time

animals = {50:"Cat",60:"Panda",70:"Dog",80:"Wolf",90:"Lion",100:"Dragon","Error":"Something is wrong about you..!! :D"}
questions = ["Do you like to go for tracking or out door activities ?","Do you like fighting movies?","Do you like to talk to people?","Do you like rock music?","Do you like to play any kind of sports ?"]


def welcome_call():
    print("\n\t/---------------------------------\\")
    print("\n\t|    Find Your Spirit Animal      |")
    print("\n\t\---------------------------------/")

def optn():
    print("Enter your option:")
    options = int(input("1) Yes\n2)Almost Yes\n3)Almost No\n4)No\n5)Not Sure\n\nYour option: "))
    score = {1:20,2:15,3:10,4:5,5:0}
    return score[options]

def animal_output(score):
    remainder = score % 10
    if remainder < 5:
        score = score - remainder
    elif remainder == 5:
        score = score + 5
    else:
        score = score +  (10 - remainder)
    return score
        
def calculating():
   string = '\n\tCalculating your score..'
   for c in string + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(.2)
     
score = 0
for question in questions:
    os.system("cls")
    welcome_call()
    print(question)
    score += optn()
    
score = animal_output(score)
calculating()
os.system("cls")
print("\n\n\tYour Spirit Animal Is: ",animals[score])
time.sleep(2)