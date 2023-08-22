from re import*
text="luminar is a technolab luminar gives nice atmosphere"
mather=finditer("luminar",text)
count=0
for m in mather:
    print(m.start())
    count+=1
print(count)
print(type(mather))