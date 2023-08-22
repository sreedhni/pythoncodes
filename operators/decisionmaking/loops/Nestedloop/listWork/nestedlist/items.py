items=[[1,"potatto",45,"veg",10],
    [1,"tomatto",40,"veg",20],
    [1,"onion",35,"veg",0],
    [1,"brinjal",50,"veg",0],
    [1,"fish",145,"nonveg",10],
    [1,"chicken",145,"nonveg",10],
    [1,"egg",6,"nonveg",100]]
# total number products
# print in stock product names
# print out of stock product names
# print veg category product names
# product available in range of 50-100
# veg products available in range of 40-80

# 1
print()

print("total no of items", len(items))
print()

# 2
in_stock=[item[1] for item in items if item[4]!=0]
print("these are in stock",in_stock)
print()
#3
out_stock=[item[1]for item in items if item[4]==0]
print("these are outof stock",out_stock)
print()
#4
veg=[item[1] for item in items if item[3]=="veg"]
print( "these are vegetables",veg)
print()
#5
veg=[item[1] for item in items if 49<item[2]<100]
print("these are available in range 50-100",veg)
print()
#6
veg=[item[1] for item in items if item[2]in range(40,81)and item[3]=="veg"]
print("these are veg products available in range 40-80",veg)
print()