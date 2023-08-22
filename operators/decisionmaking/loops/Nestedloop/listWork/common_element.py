# lst1=[8,14,15,20,21]
# lst2=[9,10,20,22,24]
# p1=0
# p2=0
# while(p1<len(lst1) and p2<len(lst2)):
#     if(lst1[p1]==lst2[p2]):
#         print(lst1[p1])
#         p1+=1
#     elif(lst1[p1]<lst2[p2]):
#         p1+=1
#     elif(lst1[p1]>lst2[p2]):
#         p2+=1
    
lst1=[8,14,15,20,21]
lst2=[9,10,20,22,24]
s1=set(lst1)
s2=set(lst2)
print(s1.intersection(s2))