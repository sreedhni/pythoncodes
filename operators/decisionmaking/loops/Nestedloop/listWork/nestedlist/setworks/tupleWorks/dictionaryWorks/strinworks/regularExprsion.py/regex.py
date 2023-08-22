sen="joel is a very good dtudent in may batch" # check the sentance is starts with joel then print the sentance starts with joel
# bol=sen.startswith("joel")
# if bol==True:
#     print("the sentance starts with joel")

# wo=sen.split(" ")
# if wo[0]=="joel":
#     print("the sentance starts with joel")

# import packageName
import re 
sen="joel is a very good dtudent in may batch"

x=re.search("^joel",sen) 
y=re.search("^Joel",sen)
# print(x)
# print(y)
x=re.search("batch$",sen)
print(x)
sten=re.search("^joel.*batch$",sen)
print(sten)
sen2="joel is a very good dtudent in may batch     "
sten=re.search("^joel.*batch$",sen2)

