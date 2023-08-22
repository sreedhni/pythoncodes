            #          *

    # c  1  2 3 4 5 6  7 8 9
# r1#             * 
# r2#           *   *        
# r3#         *   *   * 
# r4#       *   *   *   *
# r5#     *   *   *   *   *
for row in range(1,5): # 1 in(1,6)
    for col in range(1,8): 
        if(row==1)or(row+col==8)or(col==row):
            print("*",end="")
        else:
            print(end=" ")
    print()
      
