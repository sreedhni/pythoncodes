fread=open("operators//decisionmaking//loops//Nestedloop//listWork//nestedlist//setworks//tupleWorks//dictionaryWorks//strinworks//fwrite//users//data.txt","r")
user=[]
for line in fread:
    l=line.rstrip("\n")
    # print(l)
    name,folloers,following=l.split(",")
    print(name)
    print(folloers)
    print(following)