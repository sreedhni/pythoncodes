text="one 100 and fifty 5" #print digits only

for w in text.split(" "):
    if w.isdigit():
        print(w)
num=[w for w in text.split(" ") if w.isdigit()]
print(num)


text="one 100 and fifty 5"
text.split(" ")
al=[t for t in text.split() if t.isalpha()]
print(al)