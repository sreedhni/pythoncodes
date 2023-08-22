arr=[2,3,4]
tot_sum=sum(arr)
print(tot_sum,"is tot")
for ar in arr:
   print(tot_sum-ar)
op=[]
for ar in arr:
   res=tot_sum-ar
   op.append(res)
print(op)