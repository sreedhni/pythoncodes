# text="AABBCCCDE"
# # print most recursive character in given text
# wc={}
# for ch in text:
#     if ch in wc:
#         wc[ch]+=1
#     else:
#         wc[ch]=1
# print(wc)
# greatest = max(wc,key=lambda k:wc.get(k))
# print(greatest)
# smalest = min(wc,key=lambda k:wc.get(k))
# print(smalest)


text="AABBCCCDE"
# print most recursive character in given text
dic={}
for ch in text:
    if ch in dic:
        dic[ch]+=1
    else:
        dic[ch]=1
print(dic)
print(max(dic,key=lambda w:dic.get(w)))

    










