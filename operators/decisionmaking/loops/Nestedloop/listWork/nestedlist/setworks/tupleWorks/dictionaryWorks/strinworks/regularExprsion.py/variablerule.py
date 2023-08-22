from re import*
rule="[a-zA-Z_][A-Za-z0-9_]*"
varible="_hihello09_"
mathr=fullmatch(rule,varible)
if(mathr==None):
    print("invalid")
else:
    print("valid")