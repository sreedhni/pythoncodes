# Write a program that prompts the user to input their age and using if... Elif statements display 
# messages indicating their life stage
#  Child
#  Teenager
#  Adult
#  Senior citizen


# age=int(input("enter the age"))
# if age in range(1,13):
#     print("Child")
# elif age in range(13,18):
#     print("Teenager")
# elif age in range(18,30):
#     print("Adult")
# elif age in range(30,60):
    # print("Senior citizen")


# .Txt= "i have a car 2 bikes and 3 cycles."
# Write a program to extract digits from the above text.
# Output : 2,3

# from re import*
# txt = "i have a car 2 bikes and 3 cycles."
# digits =findall(r'\d+', txt)
# for digit in digits:
#     print(digit)


# Lst1=[10,11,13,15]
# Lst2=[9,8,11,13,14]
# Write an efficient program to find the common elements from the array.
# Lst1=[10,11,13,15]
# Lst2=[9,8,11,13,14]
# p1=0
# p2=0
# while(p1<len(Lst1) and p2<len(Lst2)):
#     if(Lst1[p1]==Lst2[p2]):
#         print(Lst1[p1])
#         p1+=1
#     elif(Lst1[p1]<Lst2[p2]):
#         p1+=1
#     elif(Lst1[p1]>Lst2[p2]):
#         p2+=1


# Given a text file contain number of valid and invalid passwords, create a program to write a the vaid 
# passwords to new file passwords.txt
# Validations for passwords :
# - password must contain 6 characters
# - must include one uppercase character
# - must contain a special character
from re import*
rule="[A-Z]
Password@123
abc123
@abc123
django@123
angular#$123
a@123
Password
pwd@123


