def MoveZeroes(nums):
    s = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[s],nums[i] = nums[i],nums[s]
            s+=1
    print(nums)
            # print(nums[i])

        

        
    # nums2 = []
    # for i in nums:
    #     if i == 0:
    #         nums2.append(i)
    #         nums.remove(i)
    # print(nums+nums2)
            
    
    
print(MoveZeroes([0,1,0,3,0,12]))