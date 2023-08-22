import re
mail=input("enter a mail id")
gmail=re.search("@gmail.com$",mail)
if(gmail):
    print("gmail verified")
else:
    print("gmail not verified")