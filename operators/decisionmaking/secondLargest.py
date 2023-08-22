# n1=50
# n2=9
# n3=6
# if(n1<n2) and (n3<n1):
#     print(f"{n1} is the second largest number")
# elif(n1<n3 and n1>n2):
#      print(f"{n1} is the second largest number")
# elif(n2<n3 and n2>n1):
#     print(f"{n2} is the second largest number")
# elif(n2<n1 and n3<n2):
#     print(f"{n2} is the second largest number")
# elif(n3<n2 and n1<n3):
#     print(f"{n3} is the second largest number")
# elif(n3<n1 and n3>n2):
#      print(f"{n3} is the second largest number")

num1=30
num2=6
num3=2
first=0
second=0
third=0
if((num1>num2) and (num1>num3)):
    first=num1
    if num2>num3:
        second=num2
        third=num3
    else:
        second=num3
        third=num2
elif((num2>num1) and (num2>num3)):
    first=num2
    if num1>num3:
        second=num1
        third=num3
    else:
        second=num3
        third=num1
elif((num3>num1) and (num3>num2)):
    if num1>num2:
        second=num1
        third=num2
    else:
        second=num2
        third=num1
# print(first,second,third)
# print(second )

num1=30
num2=6
num3=200
first=0
secnd=0
third=0
if num1>num2 and num1>num3:
    first=num1
    if num3<num2:
        secnd=num2
        third=num3
    else:
        secnd=num3
        third=num2
elif num2>num3:
    first=num2
    if num1>num3:
        secnd=num1
        third=num3
    else:
        secnd=num3
        third=num1
else:
    first=num3
    if num1>num2:
        secnd=num1
        third=num3
    else:
        secnd=num2
        third=num3
print(first,secnd,third)


