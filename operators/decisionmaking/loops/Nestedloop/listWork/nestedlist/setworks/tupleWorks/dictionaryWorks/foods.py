foods=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
]
fd_nme=[fd.get("name") for fd in foods ]
print(fd_nme)
fdnme=list(map(lambda fd:fd.get("name"),foods))
print(fdnme)
lst_price=list(map(lambda fd:fd.get("price"),foods))
veg=[fd.get("name") for fd in foods if fd.get("category")=="veg"]
print(veg)
vegfd=list(filter(lambda fd:fd.get("category")=="veg",foods))
print(vegfd)





















