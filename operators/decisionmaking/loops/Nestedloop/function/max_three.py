def max_three(num1,num2,num3):
#    if((num1>num2) and (num1>num3)): #6>4 and 6>
#       return(num1)
#    elif(num2>num3):
#       return(num2)
#    #  elif((num3>num1) and (num3>num2)):
#    else:
#       return(num3)
# print(max_three(6,4,5))
 return num1 if (num1>num2) and (num1>num3) else num2 if num2>num3 else num3
print(max_three(6,4,5))
 