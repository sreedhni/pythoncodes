numbers=[2,7,8,9,12,13]
odds=[]
evens=[]
for num in numbers:
    if num%2==0:
        evens.append(num)
    else:
        odds.append(num)
# evens.append(num) if num%2==0 else odds.append(num)
print(odds,"is odds")
print(evens,"is evens")



