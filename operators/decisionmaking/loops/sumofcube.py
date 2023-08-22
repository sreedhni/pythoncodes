num=153
sum=0
while(num!=0):
    digit=num%10 #3 ,2 ,1 
    print(digit) #3 ,2 ,1
    num=num//10 #12 ,1 ,0
    cube=digit**3
    sum+=cube
print("sum of the cube", sum)


