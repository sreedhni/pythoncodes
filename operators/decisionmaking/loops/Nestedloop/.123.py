for row in range(1,4): #1  #2
    for col in range(1,row+1):#1  #12
        print(col,end="") #1
    print()

    # ****     
    # ***
    # **
    # *
for row in range(1,4):
    for col in range(1,4):
        if(row==col or (row-col)==1 or (row+col==4 and row>2)):
            print(".",end=" ")
        else:
            print(end=" ")
print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()