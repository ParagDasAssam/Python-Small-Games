import string
import os,sys
import time
def input_checker(value):
    valid = ["l","r","u","d"]
    check = list(set(value))
    for i in check:
        if i not in valid:
            return False
    return True
def path_calculation(path):
    coordinate = [0,0]
    for step in path:
        if step == "r":
            coordinate[1] = coordinate[1]+1
        elif step == "l":
            coordinate[1] = coordinate[1]-1
        elif step == "u":
            coordinate[0] = coordinate[0]-1
        else:
            coordinate[0] = coordinate[0]+1
    return(coordinate)
def main_path_calculation(path,mat):
    coordinates = [0,0]
    for step in path:
        # print("Value: ",mat2[coordinates[0]][coordinates[1]])
        if mat[coordinates[0]][coordinates[1]] == "|":
            return "error"
        else:
            if step == "r":
                coordinates[1] = coordinates[1]+1
            elif step == "l":
                coordinates[1] = coordinates[1]-1
            elif step == "u":
                coordinates[0] = coordinates[0]-1
            else:
                coordinates[0] = coordinates[0]+1
    # print("Final ",coordinates)
    return(coordinates)
#level 1
def level_one():
    print("\n\tLevel 1\n")
    mat = [["#","#"],["#","&"]]
    for i in mat:
        for j in i:
            print("    "+j,end="")
        print()
    path = list(input("\nEnter path:").lower().replace(" ",""))
    validation = input_checker(path)
    if validation == True:
        final_location = path_calculation(path)
        if final_location == [1,1]:
            return ("\tLevel Cleared")
        else:
            print("You lost..!!")
            time.sleep(1)
            sys.exit()
    else:
        print("Wrong input")
        time.sleep(1)
        sys.exit()
# Level 2
def level_two():
    os.system("cls")
    print("\n\tLevel 2\n")
    mat2 = [["#","|","#"],["#","#","#"],["|","#","&"]]
    for i in mat2:
        for j in i:
            print("    "+j,end="")
        print()
    path = list(input("\nEnter path:").lower().replace(" ",""))
    validation = input_checker(path)
    if validation == True:
        final_location = main_path_calculation(path,mat2)
        if final_location == "error":
            print("You lost..!!")
            time.sleep(1)
            sys.exit()
        if final_location == [2,2]:
            return ("\tLevel Cleared")
        else:
            print("You lost..!!")
            time.sleep(1)
            sys.exit()
    else:
        print("Wrong input")
        time.sleep(1)
        sys.exit()
#level 3
def level_three():
    os.system("cls")
    print("\n\tLevel 3\n")
    mat3 = [["#","|","#","#"],["#","#","|","#"],["|","#","#","#"],["|","#","|","&"]]
    for i in mat3:
        for j in i:
            print("    "+j,end="")
        print()
    path = list(input("\nEnter path:").lower().replace(" ",""))
    validation = input_checker(path)
    if validation == True:
        final_location = main_path_calculation(path,mat3)
        if final_location == "error":
            print("You lost..!!")
            time.sleep(1)
            sys.exit()
        if final_location == [3,3]:
            return ("\tLevel Cleared")
        else:
            print("You lost..!!")
            time.sleep(1)
            sys.exit()
    else:
        print("Wrong input")
        time.sleep(1)
        sys.exit()
def main():
    situation = level_one()
    print(situation)
    time.sleep(1)
    situation = level_two()
    print(situation)
    time.sleep(1)
    situation = level_three()
    print(situation)
    # exit = input("\n\nEnter to exit")
    os.system("cls")
    print("\n\t You have cleared this game")
    time.sleep(2)
if __name__== "__main__":
  main()
