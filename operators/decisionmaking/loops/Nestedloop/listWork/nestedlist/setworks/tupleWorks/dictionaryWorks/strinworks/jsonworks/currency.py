from json import load
with open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\jsonworks\\currency.json","r")as f:
    data=load(f)
amount=int(input("enter a amount"))
sourcecode=input("enter a source code")
destinatn=input("enter a destinatn")
rates=data.get("conversion_rates")
fromrate=rates.get(sourcecode)
torate=rates.get(destinatn)
result=(amount/fromrate)*torate
print(result)
from json import load
with open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\jsonworks\\currency.json","r") as f:
    data=load(f)
rates=data.get("conversion rate")