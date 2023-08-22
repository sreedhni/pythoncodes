for row in range(1,5): # 1 in(1,6)
    for col in range(1,8): 
        if(row+col==5):# or(row+col==5)or(col-row==3):
            print("*",end="")
       # elif(row==4 and col%2!=0 and col>1):
            # print("*",end="")

        else:
            print(end=" ")
    print()


#  1 2 3 4  5 6 7
# 1      *
# 2    *   *
# 3  *       *                                              
# 4 * *  *  *  *  
