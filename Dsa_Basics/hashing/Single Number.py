def SingleNumber(nums):
    d={}
    for i in nums:
        if i in d:
            del d[i]
        else:
            d[i]=1
    print(list(d.keys())[0])
    
    
print(SingleNumber([2,2,1]))