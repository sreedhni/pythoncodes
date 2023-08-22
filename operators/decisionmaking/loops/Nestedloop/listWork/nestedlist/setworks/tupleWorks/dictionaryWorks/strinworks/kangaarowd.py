wd="supervisor"
d={}
is_kangaru=True
for w in wd:
    if w in d:
        d[w]+=1
    else:
        d[w]=1
chk="supieror"
for c in chk:
    if c in d and d[c]>0:
        d[w]-=1
    else:
        is_kangaru=False
        break
print("congaru")
 
    