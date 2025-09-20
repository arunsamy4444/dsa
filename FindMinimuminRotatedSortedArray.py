def FindMinimuminRotatedSortedArray(nums):
    l,r=0,len(nums)-1
    while l < r:
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    print(nums[m])

    
    # min = nums[0]    
    # for i in nums:
    #     if i < min:
    #         min = i
    # print(min)
       
print(FindMinimuminRotatedSortedArray([4,5,6,7,0,1,2])) #0
print(FindMinimuminRotatedSortedArray([3,4,5,1,2]))      # Output: 1
print(FindMinimuminRotatedSortedArray([11,13,15,17]))    # Output: 11