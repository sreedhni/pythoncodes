# from json import load
# with open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\jsonworks\\RESTCOUNTREES.json",encoding="UTF-8") as f:
#     data=load(f)
# print(len(data))  # no of counti
# # Print all country name
# country_name=[c.get("name") for c in data ]
# print(country_name)
#  #print region name
# region_name=set([c.get("region") for c in data])
# print(region_name)
# #asian country name
# asian_cntry=set([c.get("name") for c in data if c.get("region")=="Asia"])
# print(asian_cntry,"asian cntry")
# #population of afganistan
# populn=[c.get("population") for c in data if c.get("name")=="Afghanistan"]
# print(populn)
# capital=[c.get("capital")for c in data ]
# print(capital)
# name=[c.get("name") for c in data if c.get("capital")=="Kabul"]
# print(name)
# high_pop=max()

from json import load
with open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\jsonworks\\RESTCOUNTREES.json")as f:
    data=load(f)
print(len(data))