from re import*
txt="sjjkhccnBHHUIIaa_899"
matchr=finditer("[^a-zA-Z0-9]",txt) #^ inside the [ ] indicate exept
c=0
for m in matchr:
    c+=1
print(m.group())
print(c)