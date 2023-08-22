from re import*
f=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fileInput\\email.txt","r")
st=set()
rule="[a-zA-Z0-9][a-zA-Z0-9_$]*[@]gmail[.]com"
for l in f:
    id=l.rstrip("/n")
matchr=fullmatch(rule,id)
if matchr!=None:
    k=st.add(id)
print(st)