def TopKFrequent(nums,k):
    
    d = {}
    
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    sorted_keys = sorted(d , key=lambda x :d[x] , reverse=True)
    
    return sorted_keys[:k]
    
    
    
print(TopKFrequent([1,2,2,3,3,3] , 2)) #[2,3]