for row in range(1,4):
    for col in range(1,6):
        if (row+col)==4 or (row+col)==6 or (row+col)==8:
            print("*",end=" ")
        else:
            print(end="")
    print()