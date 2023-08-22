from re import*
text="techno lab luminar technolab luminar" # how many luminar is present
matchr=finditer("luminar",text)
c=0
for m in matchr:
    c+=1
print(c)