waist_size=30
buttex_size=85
helthparamtr=waist_size/buttex_size
print(helthparamtr)
gender="women"
if(gender=="women"):
    if(helthparamtr<=.80):
        print("low risk")
    elif(.81<=helthparamtr<=.85):
        print("moderate risk")
    elif(helthparamtr>=.85):
       print("high risk")
elif(gender=="men"):
    if(helthparamtr<=.95):
        print("low risk")
    elif(.96<=helthparamtr<=1):
        print("moderate risk")
    elif(helthparamtr>=1):
       print("high risk")

