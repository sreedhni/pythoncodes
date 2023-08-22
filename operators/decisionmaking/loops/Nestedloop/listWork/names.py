stud_name=["a","a","c","d"]
rep=0
ch_name=input("enter a name;")
for i in range(len(stud_name)):
    if(ch_name==stud_name[i]):
        stud_name[i]="anamika"
        rep=1
if (rep==0):
    stud_name.insert(1,"amal")
print(stud_name) 

