# weather=[
#     {"tvm":25},
#     {"apy":23},
#     {"kty":27},
#     {"idk":18},
#     {"ekm":29},
#     {"tsr":28},
#     {"tvm":26},
#     {"apy":22},
#     {"kty":28},
#     {"idk":19},
#     {"ekm":30},{"tsr":22},]
# wthr={}
# for dict in weather:
#     for dis,tem in dict.items():
        
#         if dis in wthr:
#             oldtem=wthr[dis]
#             if oldtem>tem:
#                 wthr[dis]=oldtem
#             else:
#                 wthr[dis]=tem


#         else:
#             wthr[dis]=tem
# print(wthr)



# print(max(wthr,key=lambda t:wthr.get(t)))
    
       
# weather=[
#     {"tvm":25},
#     {"apy":23},
#     {"kty":27},
#     {"idk":18},
#     {"ekm":29},
#     {"tsr":28},
#     {"tvm":26},
#     {"apy":22},
#     {"kty":28},
#     {"idk":19},
#     {"ekm":30},
#     {"tsr":22},]

# wh={}
# for dic in weather:
#     for k,v in dic.items():
#         if k in wh:
#             oldv=wh[k]
#             if oldv>v:
#                 wh[k]=v
#             else:
#                 wh[k]=v
        



#         else:
#             wh[k]=v
# print(wh)

# print(max(wh,key=lambda w:wh.get(w)))


weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},] 
wc={}
for c in weather:
   for k,v in c.items():
       if k in wc:
           oldv=wc[k]
           if oldv<v:
               wc[k]=v
           else:
               wc[k]=oldv
       else:
           wc[k]=v
print(wc)














w={} 
for d in weather:
    for k,v in d.items():
        if k in w:
            oldv=w[k]
            if v<oldv:
                w[k]=oldv
            else:
                w[k]=v



        else:
            w[k]=v
# print(w)




        
      
    

