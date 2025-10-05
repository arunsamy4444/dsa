def TopKFrequentWords(words,k):
    dict = {}
    for i in words:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    sorted_dict = sorted(dict.items() , key=lambda x:[-x[1],x[0]])
    
    res = []
    for i in range(k):
        res.append(sorted_dict[i][0])
    return res
    
print(TopKFrequentWords(["i","love","leetcode","i","love","coding"],2))