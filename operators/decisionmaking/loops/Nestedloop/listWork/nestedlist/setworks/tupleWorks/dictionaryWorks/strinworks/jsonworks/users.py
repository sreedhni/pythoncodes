from json import load
with open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\jsonworks\\data.json","r") as f:
    data=load(f)
names=[u.get("name") for u in data]
print(names)
maximum=max(data,key=lambda w:w.get("total"))
print(maximum)
sorted_order=sorted(data,key=lambda u:u.get("total"),reverse=True)
print(sorted_order)
bca=[u.get("name") for u in data if u.get("course")=="bca"]
print(bca)