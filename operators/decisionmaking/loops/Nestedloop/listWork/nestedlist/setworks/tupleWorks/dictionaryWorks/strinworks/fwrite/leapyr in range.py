fread=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fwrite\\nmbr","r")
fwrite=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fwrite\\leapwrt","w")
for yr in fread:
    year=int(yr.rstrip("\n"))
    if(year%100==0 and year%400==0):
        fwrite.write(str(year)+"\n")
    elif(year%100!=0 and year%4==0):
        fwrite.write(str(year)+"\n")
