def FindtheDuplicateNumber(nums):
    
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            print(nums[i])
    print('False')
 
        
    
print(FindtheDuplicateNumber([1,3,4,2,2])) #2