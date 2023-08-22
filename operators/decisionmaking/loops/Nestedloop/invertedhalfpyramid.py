for row in range(1,5):
    for col in range(1,5):
        if(row+col==5)or(row+col==4)or(row+col==3)or(row+col==2):
            print("*",end=" ")
        else:
            print(end=" ")
    print()