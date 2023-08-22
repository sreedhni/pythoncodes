import re
txt="abcd906"
chk=re.search("[a-z]{4}",txt)
print(chk)
str="3457abABCD"
s=re.search("[a-z]{2}[A-Z]{4}",str)
print(s)