expenses=[2000,8900,6577,9000,490000]
for exp in expenses:
    print(exp)

# print exp >16000
for exp in expenses:
    if exp>16000:
        print(exp,"is greater than 16000")

# highest expenses print
max_exp=max(expenses)
print(max_exp,"is max")
min_exp=min(expenses)
print(min_exp,"is min")
sum_exp=sum(expenses)
print(sum_exp,"is total sum")