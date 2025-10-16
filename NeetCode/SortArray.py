def sortArray(nums):
    swap = True
    while swap:
        swap = False
        for l in range(len(nums)-1):
            if nums[l] > nums[l+1]:
                nums[l],nums[l+1] = nums[l+1],nums[l]
                swap = True
    return nums
        
print(sortArray([10,9,1,1,1,2,3,1])) #[1,1,1,1,2,3,9,10]