# num=1634(1**4+6**4+3**4+4**4)=1634 armstone numbr
# num=153(1**3+5**3+3**3)=153
num=15
original=num
cnt=len(str(num))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit**cnt
    num=num//10
print(sum)
if(original==sum):
    print("The given nmbr is a armstone nmbr")
else:
    print("given nmbr is not a armstone nmbr")

# if(num==sum):
#       print("the given nmbr {num} is a armstone nmbr")
     