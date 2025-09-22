def MajorityElement(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    
    print(max(d,key=d.get))
    
    
print(MajorityElement([1,2,3,2,1,2,2,2,1,1,2]))