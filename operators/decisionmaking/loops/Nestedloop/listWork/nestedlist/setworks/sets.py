# set(),{} are used to define
# duplicates are not allowed
# mutable
# insertion order is not preserved
st=set()
print(st)
print()
st={2,3,4,5,5,3}
print(st)
print()
st={"hi",6,7.2,True,"hai"}
print(st)
print()
for el in st:
    print(el)
st1={1,2}
st2={4,7}
st1.update(st2)
print(st1)