def groupAnagrams(strs):
    
    grp = {}  
    for i in strs:
        key = ''.join(sorted(i))
        if key not in grp:
            grp[key] = []   
        grp[key].append(i)
    return list(grp.values())
    
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))