# text="ABABC"
# # # print(list(text))
# # # for ch in set(text):
# # #     print(text)
# # for i in list(text):
# #     for j in (text):
# #         if(i==j):
# #             print(j)
# #         break

# word={}
# cA=0
# cB=0
# cC=0
# for ch in text:
#     if ch in word:
#         print(ch,"is the 1st recursive letter")
#         break
#     else:
#         word[ch]=1
    
# word={}
# c_A=0
# c_B=0
# c_C=0
# for ch in text:
#     if(ch=="A"):
#         c_A+=1
#     elif(ch=="B"):
#         c_B+=1
#     else:
#         c_C+=1
#         print(c_A,c_B,c_C)
        

text="ABABC"
wh={}
for ch in text:
    if ch in wh:
        # print(ch,"is the recursive")  
        break
    else:
        wh[ch]=1

text="ABABC"
m={}
cA=0
cB=0
cC=0
for c in text:
    if(c=="A"):
        cA+=1
    elif(c=="B"):
        cB+=1
    else:
        cC+=1
print(cA,cB,cC)



