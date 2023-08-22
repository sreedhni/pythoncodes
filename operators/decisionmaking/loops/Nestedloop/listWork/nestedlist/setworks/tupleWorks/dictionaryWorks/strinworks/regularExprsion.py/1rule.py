#1st letter starts with k-m
#second character should be adigit which is divisible by 3
#any nmbr of character
var_name="k879mk"
rule="[k-m][3,6,9]*"
from re import*
v="Knm900"
r="[k][a-z][0-9]*"
m=fullmatch(r,v)
if m!=None:
    print("valid")
else:
    print("not valid")