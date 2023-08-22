#birds-remove
birds=["peacock","pigeon","duck","hen"]
ch_bird=input('enter a bird;')
for i in birds:
    if i==ch_bird:
        birds.remove(i)
print(birds)
 