def longestCommonPrefix(strs):
    if not strs:
        print('.........')
        return "..."
    strs.sort()
    f = strs[0]
    l = strs[-1]
    res = ''
    for i in range(min(len(f) , len(l))):
        if f[i] == l[i]:
            res+=f[i]
        else:
            break
    print(res)
    return res

print(longestCommonPrefix(["flower","flow","flight"]))  
print(longestCommonPrefix(["dog","racecar","car"]))   
print(longestCommonPrefix(["interspecies","interstellar","interstate"]))  