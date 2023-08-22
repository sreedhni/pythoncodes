txt="hello i am here in kaakkanaad" # longest word in the txt
for w in txt.split(" "):
    longest=max(w,key=lambda w:len(w))
print(w)
   