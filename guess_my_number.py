import random


def check_ckeck(choice, num):
    if choice == num:
        print "Its win !!"
    elif choice < num:
        print "Its more then the gussed number"
        num = input("Enter your choice (between 1 to 9): ")
        check_ckeck(choice, num)
    else:
        print "Its less then the gussed number"
        num = input("Enter your choice (between 1 to 9): ")
        check_ckeck(choice, num)


num = input("Enter your choice (between 1 to 9): ")
choice = random.randint(1, 9)
check_ckeck(choice, num)



input("Enter to exit")
