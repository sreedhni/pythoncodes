# n1=303
# n2=404
# n3=416
# if(n1<n2 and n2<n3):
#     print(n1,n2,n3)
# elif(n2<n1 and n1<n3):
#     print(n2,n1,n3)
# elif(n3<n2 and n2<n1):
#     print(n3,n2,n1)
# elif(n1<n3 and n3<n2):
#     print(n1,n3,n2)
# elif(n2<n3 and n3<n1):
#     print(n2,n3,n1)
# elif(n3<n1 and n1<n2):
#     print(n3,n1,n2)

n1=303999
n2=4040
n3=416
if n1<n2 and n2>n3:
    print("n2 is greatest")
elif n1>n3:
    print("n1 is grreatest")
else:
    print("n3 is greatest")

