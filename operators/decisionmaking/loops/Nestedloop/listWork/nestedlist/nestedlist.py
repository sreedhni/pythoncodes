lst=[[1,2],[5,6],[4,6],[50,45]]
# # print(len(lst))
# for sublist in lst:
#     # print("sublist is",sublist)
#     for num in sublist:
#         if num>5:
#             print(num)

allnumbers=[num for sublist in lst for num in sublist]  #list comprehension 
print(allnumbers)
numbergreaterthan5=[num for sublist in lst for num in sublist if num>5]
print(numbergreaterthan5)