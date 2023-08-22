# creating a list using 'list' keyword
food=list(("biriyani","manthi","alpham","porotta","shawarma"))
newfood=list(("biriyani","manthi","alpham","porotta","shawarma","alpham"))
print(food)
print(newfood)
print(type(food))
print(food[0])
print(food[1])
print(food[2])
print(food[3])
print(food[4])
food[2]="puttukadala"
print(food)
       #TO ADD A NEW ELEMENT TO A LIST in the last position
       # append is used
food.append("kizhi porota")
print(food)
food.append(34)
print(food)
for fud in food:
    print(fud)
