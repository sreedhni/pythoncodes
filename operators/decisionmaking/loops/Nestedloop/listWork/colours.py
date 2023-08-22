colours=["blue","green","red","yellow"]
print(len(colours))
for i in range(0,len(colours)):
    print(colours[i])
colours[1]="cyan"
print(colours)
for c in colours:
    print(c)