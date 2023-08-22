from re import*
rule="[k-m][369][a-zA-Z0-9]*"
variable="k3aff"
mathing=fullmatch(rule,variable)
if(mathing!=None):
    print("valid")
else:
    print("invalid")