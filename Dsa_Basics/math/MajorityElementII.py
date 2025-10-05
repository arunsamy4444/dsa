def MajorityElementII(nums):
    n = len(nums)
    d = {}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    res = []
    for k,v in d.items():
        if v > (n/3):
            res.append(k)
    print(res)
    
    
# Test
MajorityElementII([1,1,1,2,2,2,3,3,4,4,5])  # Output: []
MajorityElementII([1,1,1,2,2,2,1,1])        # Output: [1, 2]