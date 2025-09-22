def GroupAnagram(arr):
    d = {}

    for i in arr:
        a = ''.join(sorted(i))
        if a not in d:
            d[a] = [i]
        else:
            d[a].append(i)
    res = list(d.values())
    print(res)

    # print(d)
            
    
    
    
print(GroupAnagram(['eat','tea','tan','ate','nat','bat']))