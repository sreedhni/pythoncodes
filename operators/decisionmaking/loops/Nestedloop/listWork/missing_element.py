lst=[1,3,4,6]  # least +ve missing element(5) 
for i in range(0,len(lst)):
    if lst[0]!=1:
        print(1, "is missing")
        break
    else:   
        elmnt1=lst[i]
        elmnt2=lst[i+1]
        if((elmnt2-elmnt1)!=1):
            print(elmnt1+1,"is least missing element")
        break
