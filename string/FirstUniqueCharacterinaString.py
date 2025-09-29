def FirstUniqueCharacterinaString(s):
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k,v in enumerate(s):
        if d[v] ==1:
            return k
    # print('-1')
      
print(FirstUniqueCharacterinaString("loveleetcode"))