#methods inside dict
# to print values in a dictionary  >>> .values() is used

stdnt={"roll":1234,"name":"hari","age":32,"course":"mca"}
print(stdnt.values())


# to print keys in a dictionary  >>> .keys() is used
print(stdnt.keys())


# to print keys and values in a dictionary  >>> .items() is used
print(stdnt.items())
for k,v in stdnt.items():
    print(k,v)
# fetching values wrt key
print(stdnt.get("name"))

# by using get method if we type invalid key then it will print a output "none" and then the next line exucution will takes place. 


# to remove a key from dictionary >> .pop() is used .pop(key name)
stdnt.pop("course")
print(stdnt)

# key()
# values()
# items()
# get(key)
# pop(key)
