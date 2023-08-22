# 
# st1=set()
# st2=set()
# for name1 in f1:
#     line1=name1.rstrip("\n")

#     st1.add(name1)
# for name2 in f2:
#     line2=name2.rstrip("\n")
#     st2.add(name2)
# print(st1)
# print(st2)
# print(st1.difference(st2))

f1=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fileInput\\total","r")
f2=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fileInput\\present","r")
st1=set(f1)
st2=set(f2)
m=(st1.difference(st2))

