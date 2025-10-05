def Subsets(nums):
    res = [[]]
    for i in nums:
        temp = []
        for j in res:
            a = j + [i]
            temp.append(a)
        res+=temp  
    return res
    
    
print(Subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]]