import random
import time
import os

def converter(optn):
    if optn == "r":
        optn = "Rock"
    elif optn == "s":
        optn = "Scissor"
    elif optn == "p":
        optn = "Paper"
    else:
        optn = "error"
    return optn

player = 0
computer = 0

print("\n\tthe game will be of 3 points only..!!\n\n")
while(player !=3 and computer != 3):
    
    print("Points\nPlayer:"+str(player)+"\nComputer:"+str(computer)+"\n")
    optn = input(" \"r\" for Rock\n \"p\" for Paper\n \"s\" for Scissor:\nYour optn: ")
    C_optn = random.choice(["Rock",'Paper',"Scissor"])
    optn = converter(optn)
    if optn != "error":
        print("\nPlayer:",optn," Computer:",C_optn)
    
    if(optn == "Rock"):
        if(C_optn == "Paper"):
            print("computer wins this round!!")
            computer += 1
        elif(C_optn == "Scissor"):
            print("player wins this round!!")
            player += 1
        else:
            print("No points beacuse both had",C_optn)
            
    elif(optn == "Paper"):
        if C_optn == "Scissor":
            print("computer wins this round!!")
            computer += 1
        elif C_optn == "Rock":
            print("player wins this round!!")
            player += 1
        else:
            print("No points beacuse both had",C_optn)
            
    elif(optn == "Scissor"):
        if C_optn == "Rock":
            print("computer wins this round!!")
            computer += 1
        elif C_optn == "Paper":
            print("player wins this round!!")
            player += 1
        else:
            print("No points beacuse both had",C_optn)
            
    else:
        print("error")
        
    if(player == 3):
        os.system('cls')
        time.sleep(1)
        print("\n\tPlayer wins !!!\n")
        time.sleep(2)
        break
    elif(computer == 3):
        os.system('cls')
        time.sleep(1)
        print("\n\tComputer wins !!!\n")
        time.sleep(2)
        break
    
    time.sleep(2)
    os.system('cls')
