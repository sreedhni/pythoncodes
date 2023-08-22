users=["sachin","kohli","sehwag","rahul","dhoni","raina"]
sachin_followers=["kohli","sehwag","rahul"]
Requst_sugetion_sachin=[]
for suggetions in users:
    if suggetions !="sachin"and suggetions not in sachin_followers:
        Requst_sugetion_sachin.append(suggetions)
print(Requst_sugetion_sachin)
