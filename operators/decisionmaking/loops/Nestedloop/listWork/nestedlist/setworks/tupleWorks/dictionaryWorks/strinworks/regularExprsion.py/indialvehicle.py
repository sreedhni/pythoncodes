from re import*
rule="[A-Z][A-Z][-][0-9]{2}[-][a-z]{1,2}[-][0-9]{4}"
val="KL-08-bn-49700"
mthr=fullmatch(rule,val)
if mthr==None:
    print("non indin")
else:
    print("indian")
