# how many ab are on the below text
from re import*
text="ababcdab"
count=0
matcher=finditer("ab",text)
for m in matcher:
    print(m.group())
    print(m.start())
    count+=1
    print(count)

