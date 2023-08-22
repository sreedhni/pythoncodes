# import re
# mobnum="94 9048075355"

# check=re.search("^91",mobnum)
# if check:
#     print("indian num")
# else:
#     print("not indian")

import re
resi=input("enter a residence number")
ekm=re.search("^0484",resi)
ijk=re.search("^0480",resi)
tcr=re.search("^0487",resi)
mpr=re.search("^0494",resi)
ksd=re.search("^04994",resi)
cct=re.search("^0495",resi)
if ekm:
    print("ekm")
elif ijk:
    print("ijk")
elif tcr:
    print("tcr")
elif mpr:
    print("mpr")
elif ksd:
    print("ksd")
elif cct:
    print("cct")