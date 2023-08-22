# 1stquestion

l=[]
for i in range(3):
    nam=input("name:")
    l.append(nam)

while(True):
    k=input("do you want to enter further names yes or no:")
    if(k.lower()!="yes"):
        break
    n=input("name of:")
    l.append(n)
print(f"there are {len(l)} people invited")

# output

# name:wDDW
# name:WDWED
# name:EFEWF
# do you want to enter further names yes or no:YES
# name of:erge
# do you want to enter further names yes or no:yes
# name of:dsw
# do you want to enter further names yes or no:no
# there are 5 people invited

# 2nd question

l=[]
for i in range(3):
    nam=input("name:")
    l.append(nam)

while(True):
    k=input("do you want to enter further names yes or no:")
    if(k.lower()!="yes"):
        break
    n=input("name of:")
    l.append(n)
print(l)
se=input("enter the name to be searched:")
ask=input(" do they still want that person to come to the party yes or no:")
if ask.lower()=="no":
    l.remove(se)
print(l)

# output
# name:s
# name:s
# name:d
# do you want to enter further names yes or no:yes
# name of:e
# do you want to enter further names yes or no:no
# ['s', 's', 'd', 'e']
# enter the name to be searched:d
#  do they still want that person to come to the party yes or no:no
# ['s', 's', 'e']

# question 3
# list=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]] 
# k=int(input("enter the row to bes displayed:"))
# print(list[k])

# # output
# # enter the row to bes displayed:1
# # [3, 7, 4]


# 4th question
l=[]
for i in range(4):
    dic={}
    na=input("enter the name:")
    dic["name"]=na
    age=int(input("enter the age:"))
    dic["age"]=age
    id=int(input("enter id:"))
    dic["id"]=id
    l.append(dic)
search=input("enter the name to be searched:")
for i in l:
    if i["name"]==search:
        print(i)
    
# output:
# enter the name:s
# enter the age:3
# enter id:1
# enter the name:e
# enter the age:3
# enter id:4
# enter the name:f
# enter the age:2
# enter id:2
# enter the name:f
# enter the age:3
# enter id:3 
# enter the name to be searched:f     
# {'name': 'f', 'age': 2, 'id': 2}    
# {'name': 'f', 'age': 3, 'id': 3} 

# 5th question
l=[]
for i in range(4):
    dic={}
    na=input("enter the name:")
    dic["name"]=na
    age=int(input("enter the age:"))
    dic["age"]=age
    id=int(input("enter id:"))
    dic["id"]=id
    l.append(dic)
    print(dic)
for i in l:
    print(f"name={i['name']} age={i['age']}")
    
# output
# enter the name:d
# enter the age:5
# enter id:4
# enter the name:t
# enter the age:5
# enter id:4
# enter the name:g
# enter the age:7
# enter id:8
# enter the name:h
# enter the age:8
# enter id:6
# [{'name': 'd', 'age': 5, 'id': 4}, {'name': 't', 'age': 5, 'id': 4}, {'name': 'g', 'age': 7, 'id': 8}, {'name': 'h', 'age': 8, 'id': 6}]        
# name=d age=5
# name=t age=5
# name=g age=7
# name=h age=8

# question6

dic={"inferno":{"author":"Dan Brown","publication year":2001, "genre":"scientific"},"da vinci code":{"author":"Dan Brown","publication year":2001, "genre":"scientific"}}
k=input("do you want to add a new book yes or no")
if k.lower()=="yes":
    title=input("enter the book title")
    auth=input("enter the author")
    til={}
    til["author"]=auth
    pub=input("enter the year")
    til["publication year"]=pub
    gen=input("enter the genre")
    til["genre"]=gen
    dic[title]=til
print(dic)

u=input("enter the book to be updated:")
for i in dic:
    
    if i==u:
        w=input("enter what you want to update:")
        k=input(f"enter the {w}:")
        dic[i][w]=k
print(dic)
print(len(dic))
# output
# do you want to add a new book yes or noyes
# enter the book titlerurk
# enter the authorfore
# enter the year2000
# enter the genredrama
# {'inferno': {'author': 'Dan Brown', 'publication year': 2001, 'genre': 'scientific'}, 'da vinci code': {'author': 'Dan Brown', 'publication year': 2001, 'genre': 'scientific'}, 'rurk': {'author': 'fore', 'publication year': '2000', 'genre': 'drama'}}
# enter the book to be updated:inferno
# enter what you want to update:author
# enter the author:dan
# 3