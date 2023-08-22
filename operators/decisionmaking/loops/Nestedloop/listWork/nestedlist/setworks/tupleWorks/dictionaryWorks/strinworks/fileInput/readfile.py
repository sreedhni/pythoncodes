f=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fileInput\\data.txt","r")
words=[]
for line in f:
    line=line.rstrip("\n").split(" ")  #rstrip used to remove a word from right side
    # w=line.split(" ")
    for m in line:
       
        words.append(m)
print(words)
