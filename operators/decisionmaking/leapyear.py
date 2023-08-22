year=2000
if((year%4==0 or year%400 ==0) and year%100!=0):
    print(year,"is a leap year")
else:
    print(year, "is not aleap year")


# All years evenly divisible by 4 are leap years.
# EXCEPT years that are also evenly divisible by 100, are NOT leap years.
# EXCEPT years that are also evenly divisible by 400 ARE leap years.
yr=2000
if((yr%4==0 or yr%400==0) and (yr%100!=0)):
    print(yr,"is leap")
else:
    print(yr,"is not leap")

