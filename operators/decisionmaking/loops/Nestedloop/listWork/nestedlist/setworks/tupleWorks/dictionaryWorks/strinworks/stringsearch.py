# # check if egg can form from eagle
# wd="eagle"
# empty={}
# for w in wd:
#     if w in empty:
#         empty[w]+=1
#     else:
#         empty[w]=1
# print(empty)
# input="egg"
# for m in input:
#     if m in empty:
#         empty[w]-=0
#     else:
#         print
    
word="observe"
d={}
is_kangaru=True
for w in word:
    if w in d:
        d[w]+=1
    else:
        d[w]=1

chk="seeee"
for m in chk:
    if m in d and d[m]>0:
        d[m]-=1
    else:
        is_kangaru=False
        break
print("is kangaru")
    

