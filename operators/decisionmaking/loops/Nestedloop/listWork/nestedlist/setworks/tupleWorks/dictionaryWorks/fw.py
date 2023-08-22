data={"django":"framework","react":"library","fastapi":"framework","vue":"framework","ajax":"library"}
# wc={}

# for value in data.values():
#     if value in wc:
#         wc[value]+=1
#     else:
#         wc[value]=1
        
# print(wc)
# for value in data.values():
wc={}
for k,v in data.items():
    if v in wc:
        wc[v].append(k)

    else:
        wc[v]=[k]
print(wc)

