for row in range (1,5):
    for col in range(1,8):
        if(row+col==8) or (row+col==6 and row<4) or (row+col==4 and row<3) or (row+col==2 and row<2):
            print("*",end="")
        elif(col-row==3)and(row>4):
            print("*",end="")
        else:
            print(end=" ")
    print()
          