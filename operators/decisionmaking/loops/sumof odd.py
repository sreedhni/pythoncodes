# start=1
# limit=10
# evensum=0
# oddsum=0
# while(start<limit):
#     if(start%2==0):
#         evensum+=start
#     else:
#        oddsum+=start
#     start+=1 
# print("sum of odd numbers", oddsum)
# print("sum of even numbers",evensum)
    
    

# start+=1
#assignmnt check is it possible to find 
start=1
limit=6
odd_sum=0
even_sum=0
for num in range(start,limit):
    if(num%2==0):
        even_sum+=num
    else:
        odd_sum+=num
print("odd sum",odd_sum)
print("even sum",even_sum) 




i=0
l=11
os=0
es=0
for m in range(i,l):
    if m%2==0:
        es+=m
    if m%2!=0:
        os+=m
print(os,"it is odd sum")
print(es,"it is even sum")