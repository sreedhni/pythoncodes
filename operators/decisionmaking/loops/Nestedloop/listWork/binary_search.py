# lst=[3,4,6,7,8,9,23] # check 1 is present or not in the list
# elmnt=1
# is_found=False
# low=0
# upper=len(lst)-1
# while(low<=upper):
#     mid=(low+upper)//2
#     if elmnt==lst[mid]:
#         is_found=True
        
#         break
#     elif(elmnt<lst[mid]):
#         upper=mid-1
#     elif(elmnt>lst[mid]):
#         low=mid+1
# print("found" if is_found==True else "not found")
    
ls=[1,2,3,6,7,8,4]
e=23
l=0
u=len(ls)-1
while(u>l):
    m=(l+u)//2
    is_found=False
    if e==ls[m]:
        is_found=True
        break
    elif e>=ls[m]:
        l=m+1
    elif e<ls[m]:
        u=m-1
print("found" if is_found==True else "not found" )

    

