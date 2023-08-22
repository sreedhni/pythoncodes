lst=[1,2,3,4,5]
# map(funtion, iterable)
squre=list(map(lambda n:n**2,lst))
print(squre)
cube=list(map(lambda n:n**3,lst))
print(cube)


def squre(n):
    return n**2
squre=list(map(squre,lst))
print(squre)