# lst=[1,3,4,8,9]
# elmnt=3
# is_found=False
# for i in range(0,len(lst)):
#     if elmnt!=lst[i]:
#         is_found=True
#         break
# print("found" if is_found==True else "not found")
# def fizzBuzz(n):
n=int(input("enter a number"))
if(n%3==0 and n%5==0):
    print("FizzBuzz")
elif(n%3==0 and n%5!=0):
    print("Fizz")
elif(n%5==0 and n%3!=0):
    print("Buzz")
elif(n%3!=0 and n%5!=0):
    print(n)
  
