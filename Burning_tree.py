def coordinate(x,y):
    result = "("+str(x)+","+str(y)+")"
    return result

def Print_forest(r_end,c_end,Forest,optn):
    if optn == 2:
        for i in range(r_end):
            for j in range(c_end):
                print("",Forest[i][j],coordinate(i,j),end=" ")
            print()
    else:
        for i in range(r_end):
            for j in range(c_end):
                print("",Forest[i][j],end=" ")
            print()
def Validation(r_end,c_end,Forest):
    for i in  range(r_end):
        for j in range(c_end):
            if Forest[i][j] == "#":
                return 1
    return 2
        
print("\n\tBurning Free")
print("Try giving a large number")
r_end,c_end = map(int,input("Enter raw and column: ").split())
print("Rows:",r_end,"Columns:",c_end)
Forest = [["#" for i in range(c_end)] for j in range(r_end)]

Print_forest(r_end,c_end,Forest,2)
print("\n\n")
Print_forest(r_end,c_end,Forest,1)
print()
while(1):
    try:
        r,c = map(int,input("Enter the coordinates(with spaces): ").split())
        if r > r_end or c > c_end:
            print("No such coordinate exist.\nPlease enter again:\n")
            continue
        for i in range(r,r_end):
            Forest[i][c] = "@"
        for j in range(c,c_end):
            Forest[r][j] = "@"
        for i in range(r,-1,-1):
            Forest[i][c] = "@"
        for i in range(c,-1,-1):
            Forest[r][i] = "@"
        print("\n")
        Print_forest(r_end,c_end,Forest,2)
        print("\n\n")
        Print_forest(r_end,c_end,Forest,1)
        print()
        validate = Validation(r_end,c_end,Forest)
        if validate == 2:
            break
        ending = input("Enter 1 to exit or enter to continue:")
        if ending == "1":
            break
    except:
        print("Your entry was wrong...\nTry again")
print("\n\nFinal:")
Print_forest(r_end,c_end,Forest,1)
print()
input("Enter to exit")