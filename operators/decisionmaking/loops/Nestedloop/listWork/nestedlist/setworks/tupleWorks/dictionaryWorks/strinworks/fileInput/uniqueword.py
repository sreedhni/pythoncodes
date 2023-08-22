f=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fileInput\\data2.txt","r")
st=set()
for l in f:
    m= l.rstrip("\n").split(" ")
    for k in m:
        wd=st.add(k)
print(st)