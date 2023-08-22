birds=["sea gull","crow","hen","duck","peacoack"]
print(birds[0])
print(birds[1])
print(birds[2])
print(birds[3])
print(birds[4])
birds[2]="penguin"
print(birds)
birds[4]="hen"
print(birds)
if birds[2]=='penguin':
    birds[2]="iam a penguin"
else:
    birds[2]="iam not penguin"
print(birds)