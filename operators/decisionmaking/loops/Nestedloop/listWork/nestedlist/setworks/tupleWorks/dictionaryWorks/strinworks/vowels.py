wods="hi hello goodmorning how are U" # vowels in the txt
vowels=["a","i","o","u",'A',"I","O","U"]
for w in wods.split():
    
    if w[0] in vowels:
        print(w)
        
vov=[w for w in wods.split() if w[0].casefold() in vowels]
print(vov)

w="hi hello goodmorning how are U"
v=["a","e","i","o","u","A","E","I","O","U"]
m=w.split(" ")
if m[0] in v:
    print(m)