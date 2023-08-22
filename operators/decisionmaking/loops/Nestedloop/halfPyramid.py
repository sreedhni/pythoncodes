for row in range(1,5):
    for col in range(1,5):
        if(row==col)or (row-col==1) or (row-col==2) or(row-col==3):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
