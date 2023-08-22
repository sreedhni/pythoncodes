# from  re import*
# rule="[k][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
# val="KL-08-bn-49700"
# mthr=fullmatch(rule,val)
# if mthr==None:
#     print("non kerala vehicle")
# else:
#     print("kerala vehicle")


from re import*
rule="[K][L][-][0-9][0-9]-[A-Z]{2}[0-9]{4}"
v=input("enter a number")
m=fullmatch(rule,v)
if m==None:
    print("non kerala")
else:
    print("kerala")