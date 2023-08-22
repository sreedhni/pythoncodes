from json import load
with open("operators//decisionmaking//loops//Nestedloop//listWork//nestedlist//setworks//tupleWorks//dictionaryWorks//strinworks//jsonworks//movies//mdb.json","r") as f:
    movie=load(f)
film=[m.get("title")for m in movie]
print(film) #all movie name
print(len(movie)) #total movie
genere=set([g for m in movie for g in m.get("genres")])
print(genere)
moviename=max(movie,key=lambda u:int(u.get("runtime")))
print(moviename.get("title"))
# inbtwn=[m.get("title") for m in movie if "crime" in m.get("genres")]
# print(inbtwn)
komedy=[m.get("title")for m in movie if "C rime" in m.get("genres")]
print(komedy)
GENREFILTER=set([m.get("title")for m in movie for g in m.get("genres") if g in ['Comedy','Fantasy']])
print(GENREFILTER)
# YEar wise movie count
yr_movie={}
for m in movie:
    yr=m.get("year")
    if yr in yr_movie:
        yr_movie[yr]+=1
    else:
        yr_movie[yr]=1
print(yr_movie)
print(max(yr_movie,key=lambda n:yr_movie.get(n)))
sortd=sorted(yr_movie,key=lambda n:yr_movie.get(n))
print(sortd)


