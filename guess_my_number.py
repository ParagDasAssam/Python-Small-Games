import random,os
os.system("cls")
def check_ckeck(choice, num):
    if choice == num:
        print ("Its correct !!")
        return True
    elif choice < num:
        print ("Its more then the gussed number")
        return False
    else:
        print ("Its less then the gussed number")
        return False        
choice = random.randint(1, 9)
answer = False
while(answer != True):
    num = int(input("Enter your choice (between 1 to 9): "))
    answer = check_ckeck(choice, num)
exit = input("Enter to exit")
