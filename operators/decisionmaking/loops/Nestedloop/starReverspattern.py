    # ****
    # ***
    # **
    # *
for col in range(4,0,-1):  #4-c,             3-c
    for row in range(col): #4-r, 3-r,2
        print("*",end="")
    print()

             #OR

for row in range(1,5):
    for col in range(5,row,-1):
        print("*",end="")
    print()


