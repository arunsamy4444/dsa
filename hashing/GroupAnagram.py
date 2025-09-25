def GroupAnagram(strs):
    
    d={}
    for i in strs:
        key = ''.join(sorted(i))
        if key not in d:
            d[key]=[i]
        else:
            d[key]+=[i]
        print(list(d.values()))

  
    
    
    
print(GroupAnagram(['eat','tea','tan','ate','nat','bat']))








  # d = {}

    # for i in arr:
    #     a = ''.join(sorted(i))
    #     if a not in d:
    #         d[a] = [i]
    #     else:
    #         d[a].append(i)
    # res = list(d.values())
    # print(res)

    # # print(d)
            