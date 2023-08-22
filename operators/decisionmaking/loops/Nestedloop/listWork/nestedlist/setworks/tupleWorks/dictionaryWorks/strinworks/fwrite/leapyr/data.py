f=open("C:\\Users\\user\\OneDrive\\Desktop\\pythoncodes\\operators\\decisionmaking\\loops\\Nestedloop\\listWork\\nestedlist\\setworks\\tupleWorks\\dictionaryWorks\\strinworks\\fwrite\\leapyr\\data","w")
years=[2000,2024,1991,1995,1200,1400,1234]
for yr in years:
    if (yr%100==0 and yr%400==0):
        f.write(str(yr)+"\n")
       
    elif(yr%100!=0 and yr%4==0):
        f.write(str(yr)+"\n")
        
