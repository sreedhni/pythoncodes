# lst=[2,3,4,4,5,7,5,6,7,7]
# find duplicate elements from the list
lst=[2,7,3,4,2,4,5,5,6,7]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            print(lst[i])


















































