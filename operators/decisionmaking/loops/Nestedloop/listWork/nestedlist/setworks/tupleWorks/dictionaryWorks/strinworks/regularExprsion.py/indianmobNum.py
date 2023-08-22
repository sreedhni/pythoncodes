import re
nmbr=input("enter ur mobile nmbrwith country code:")
x=re.search("^[+]91",nmbr)
if(x):
    print("mobile numbr is indian")
else:
    print("mobile nmbr is non indan")