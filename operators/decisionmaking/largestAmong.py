num1=100
num2=3000
num3=500
if((num1>num2) and (num1>num3)): #10>30 and 10>50 -->f and f --->f
    print("num1 is max")
if (num2>num3): #30>10 and 30>50 -->t and f --->f
    print("num2 is max")
if((num3>num1) and (num3>num2)): #50>10 and 50>10  --->t and t -->t
    print("num3 is max") # print num3

def ma(*args):
    return max(*args)
print(ma(8,66,777,889))
print(ma(4,7))


