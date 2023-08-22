# def prime_nmbr(num1):
#     for i in range(2,num1):
#         if(num1%i!=0):
#             return("prime")
#         else:
#             return("not prime")
# print(prime_nmbr(9))

def prime(num):
    is_prime=True
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
    return "prime number" if is_prime==True else "not prime"
