itemss= [
    {"sugar": 45},
    {"tea_powder": 28},
    {"coffee": 67},
    {"dairymilk": 170},
    {"kitkat": 70},
    {"bourborn": 50},
    {"munch": 30},
    {"milk": 80},
    {"pepsi": 99},

]


offers=[
    {"sugar":10},
    {"cofee":20},
    {"milk":5},
    {"pepsi":10}]

for itm in itemss:   
    for ofr in offers:
        for k,v in itm.items():
              if k in ofr:
                itm[k]-=ofr.get(k)
print(itemss)






