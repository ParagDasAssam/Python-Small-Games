mat2 = [["#","|","#","#"],["#","#","|","#"],["|","#","#","#"],["|","#","|","&"]]
for i in mat2:
    for j in i:
        print("    "+j,end="")
    print()

coordinate = [0,0]
path = list(input("\nEnter path: ").lower().replace(" ",""))

for step in path:
    if step == "r":
        coordinate[1] = coordinate[1]+1
    elif step == "l":
        coordinate[1] = coordinate[1]-1
    elif step == "u":
        coordinate[0] = coordinate[0]-1
    else:
        coordinate[0] = coordinate[0]+1

print(coordinate)
print(coordinate[0],type(coordinate[0]))
print(mat2[coordinate[0]][coordinate[1]])
print(mat2)

# print(mat2[coordinate[0],coordinate[1]])
exit = input("")