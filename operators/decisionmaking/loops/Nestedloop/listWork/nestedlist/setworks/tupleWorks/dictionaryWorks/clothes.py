clothes=[
    {"item":"shirt","brand":["allen solly","us polon","peter england"],"sizes":["s","l"],"colour":"black"},
    {"item":"tshirt","brand":["allen solly","us polon","peter england","nike","adidas"],"sizes":["s","XL"],"colour":["black","green","red"]},
    {"item":"pant","brand":["Louis Philippe","peter england"],"sizes":["XL","l"],"colour":["black","grey","blue"]},
    {"item":"saari","brand":["kalanjali","satya paulsarees","mimos sarees"],"sizes":["5m","6m"],"colour":["black","grey","blue","green"]},

    
    ]
for cloth in clothes:
    print(cloth["item"])
cloth_name=[cloth.get("item") for cloth in clothes]
print(cloth_name)

for cloth in clothes:
    if cloth["colour"]=="grey":
        print(cloth["item"])
    if "allen solly" in cloth["brand"]:
        print(cloth["item"])
allensolly_nm=[cloth.get("item") for cloth in clothes if "grey" in cloth["colour"]]
print(allensolly_nm)
