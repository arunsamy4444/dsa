def findDuplicate(nums):
    seen = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            print(i)

 
             
    # for i in range(0,len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] == nums[j]:
    #             return nums[i]

    
print(findDuplicate([1,3,4,2,2]))