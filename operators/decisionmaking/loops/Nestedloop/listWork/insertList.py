# lst=[2,3,4,5]
# lst.append(6)
# print(lst)
  
#      # insert -to add to a particular position in a list
# lst.insert(3,1)  # listname.insert(position of list,value to be added to list)
# print(lst)
emptylst=[]
print(emptylst)
length=int(input("enter the value:"))
for i in range(length):
    num=int(input(f"enter the {i}th position value"))
    emptylst.append(num)
print(emptylst)
max_empty=max(emptylst)
print(max_empty)
maxim=max_empty+int(10)
emptylst.insert(2,maxim)
print(emptylst)


