# sum of 10 numbers
num=1
sum=0
while(num<=10):
    sum+=num #sum=sum+num.....   =0+1+2+3....
    num+=1   #num=num+1 ............1+1, 2+1,    
# print("sum of 10 natural numbers",sum)
num=0
sum=0

for num in range(1,10):
    num+=1
    sum+=num
print(sum)
    