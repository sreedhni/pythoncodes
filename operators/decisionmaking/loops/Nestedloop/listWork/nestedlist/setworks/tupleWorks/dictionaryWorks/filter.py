lst=[1,2,3,34,5,6]
odds=list(filter(lambda n: n%2!=0,lst))
print(odds)
evens=list(filter(lambda n:n%2==0,lst))
print(evens)
gt3=list(filter(lambda n:n>3,lst))
print(gt3)

# filter is used if ther exixt any conditions
