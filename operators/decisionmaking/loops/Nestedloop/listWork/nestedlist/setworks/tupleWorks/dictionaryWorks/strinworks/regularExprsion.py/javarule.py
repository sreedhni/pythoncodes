from re import*
rule="[a-zA-Z][a-zA-Z0-9_$]{1,15}"
varible="_a$0_90000"
mathr=fullmatch(rule,varible)
if mathr==None:
    print("invalid")
else:
    print("valid")