# # *args positional argument takes any number of parameters type tuple
# def addition(*args):
#     return sum(args)
# print(addition(3,4))
# print(addition(6,9,10))
# addition=lambda *args:sum(args)
# print(addition(3,6,1))
def add(*args):
    return sum(args)
print(add(8,7,9))
