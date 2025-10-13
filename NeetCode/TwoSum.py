def TwoSum(nums,target):
    
    d = {}
    
    for i,num in enumerate(nums):
        res = target - num
        if res in d:
            return [d[res],i]
        d[num] = i
    
    
print(TwoSum([3,4,5,6], 7))