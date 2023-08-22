for row in range (1,5):   # 1
    for col in range(1,8): # 1
        if(row+col==5) or (row+col==7 and row>1) or (row+col==9 and row>2) or (row+col==11 and row>3): # if (f)or (f)or
            print("*",end="")
        else:
            print(end=" ")
    print()
 

# for row in range(1,5):
#     for col in range(1,8):
#         if (col+row==5) or (row+col==7 and row>1) or (row+col==9 and row>2) or(row+col==11 and row>3):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()
#  1234567
#1    *   
#2   * *  
#3  * * * 
#4 * * * *

# for row in range(1,5):
#     for col in range(1,8):
#         if(col+row==5) or (col+row==7 and row>1) or(col+row==9 and row>2) or (col+row==11 and row>3):
#             print(".",end="")
#         else:
#             print(end=" ")
#     print()


# rows=int(input("enter row:"))
# for row in range(rows):
#     for col in range(row+1):
#         print('*',end=" ")
#     print('\n')    

rows=int(input("enter row:"))
for i in range(1,rows,1):
    print(" * " *i)