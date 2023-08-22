f=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fileInput\\data1.txt","r")
# for line in f:
#     print(line)
# add the words into a list
wd=[]
for l in f:
    m=l.rstrip("\n").split(" ")   #rstrip used to remove from right side ,lstrip used to remove in left side
    wd.append(m)
print(wd)