from re import*
text="ababcdababcfabghab"
matchr=finditer("ab",text)
c=0
print(matchr)
for m in matchr:
    print(m.group()) #it will give which group will match
    print(m.start()) #it will starting location of ab
    c+=1
print(c)