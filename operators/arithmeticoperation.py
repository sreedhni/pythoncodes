""""
1 arithmetic operation
      addition +,
      substraction -,
      division /,
      multiplication *,
      modulus %,
      exponentiation **,
      floor division //,
"""
      # 1)addition
num1=20
num2=30
sum=num1+num2
print(sum)
#sum of 20+30 is 50
print(f"sum of {num1}+{num2} is {sum}")
print(type(sum))
num1=1.5
num2=3.5
sum=num1+num2
print(sum)
print(type(num1))
print(type(sum))
#sum of 1.5 and num 3.5 is float type
print(f"sum of {num1} and {num2} is flot type")
     # 2)substraction
num1=20
num2=40
diff=num2-num1
sub=num1-num2
#40-20=20
print(f"{num2}-{num1} = {diff}")
#20-40=-20
print(f"{num1}-{num2} = {sub}")
#-20 is a negative number
print(f"{sub} is a negative number")
print(type(sub))
     # 3)division
n1=40
n2=20
n3=25
div1=n1/n2
div2=n2/n3
print(f"{n1}/{n2} = {div1}")
print(f"{n2}/{n3}={div2}")
print(type(div2))
    #4)multiplication
n1=40
n2=20
multi=n1*n2
print(f"{n1}*{n2} = {multi}")
    #5)modulus
num1=35
num2=10
rem=num1%num2
print(f"{num1} % {num2} = {rem}")
   #6)exponential
number=2
power=5
value=number**power
print(f"{number} ** {power} = {value}")
    #7)floor division
num1=10
num2=30
result=num1//num2
print(f"{num1}//{num2} = {result}")
print(num1//num2)

