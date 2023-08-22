mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]]
print(f"{len(mobiles)}mobiles avalable") #total number of mobiles
for sublist in mobiles:
    print(sublist[1])
print()
mobile_names=[mob[1] for mob in mobiles] #list comprehension, mobile names
print(mobile_names)
print()
mobile_names=[mob[1] for mob in mobiles if mob[3]=="4g"] #4g mobiles only
print(mobile_names)
print()
filter_mobiles=[mob[1] for mob in mobiles if mob[2]<30000] #mobiles which have price less than 30k
print(filter_mobiles)
print()
 
filter_mobiles=[mob[1] for mob in mobiles if 30000<mob[2]<50000]  #mobiles which have price in between 30k and 50k
print(filter_mobiles)
print()
# filter_mobiles=[mob[1] for mob in mobiles if mob[2] in range(30000,500001)] 
# filter_mobiles=[mob[1] for mob in mobiles if mob[2]>30000 and mob[2]<50000] 
filter_mobiles=[mob[1] for mob in mobiles if 25000>mob[2] and mob[3]=="5g"]  #mobile name which have price below 25000 and which have 5g
print(filter_mobiles)
print()