num=123
sum=0
while(num!=0):
    digit=num%10 #3 ,2 ,1 
    print(digit) #3 ,2 ,1
    num=num//10 #12 ,1 ,0
    # sum+=digit  #0+3+2+1=6
# print("sum of digit",sum)
    cube=digit**3
    sum+=cube
print(sum)



