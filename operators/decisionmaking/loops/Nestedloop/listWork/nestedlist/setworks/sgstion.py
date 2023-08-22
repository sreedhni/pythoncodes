alluser=["mohanlal","fahad","dq","vijay","nivin","asif"]
dq_frnds=["mohanlal","fahad","asif"]
dq_sgst=set(alluser).difference(set(dq_frnds))
# print(sgst)
dq_sgst.remove("dq")
print("dq gets suggestions from",dq_sgst)
print()

asif_frnds=["mohanlal","fahad","vijay","nivin"]
mutual=set(dq_frnds).intersection(set(asif_frnds))
print("mutual friends are",mutual)
  

