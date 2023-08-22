num1=10
num2=20
print(f"values b4 swapping num1={num1} num2={num2}") #num1=10 num2=20
#logic 1

# temp=num1
# num1=num2num2=temp
# num2=temp
#logic 2

(num1, num2)=(num2,num1)
print(f"values after swapping num1={num1} num2={num2}")
#logic3

num1=num1+num2 #10+20=30
num2=num1-num2 #30-20=10
num1=num1-num2 #30-10=20
print(f"values after swapping num1={num1} num2={num2}")


