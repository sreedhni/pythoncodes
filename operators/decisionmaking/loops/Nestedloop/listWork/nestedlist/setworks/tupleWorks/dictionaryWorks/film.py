movies={"2018":5,"keralastory":3,"neymar":4,"kgf":5,"arm":4}
#print all movie
print(movies.keys()) 



#  top rated movie
# print(max(movies,key=lambda k :movies.get(k)))

# # sort

# print(sorted(movies,reverse=True,key=lambda k:movies.get(k)))




top=max(movies,key=lambda k:movies.get(k))
print(top)
so=sorted(movies,key=lambda k:movies.get(k))