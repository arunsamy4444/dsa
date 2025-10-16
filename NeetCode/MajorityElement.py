def majorityElement(nums):
    d = {}
    
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    res = max(d, key=d.get)
    print(res)
    
    
print(majorityElement([5,5,1,1,1,5,5]))