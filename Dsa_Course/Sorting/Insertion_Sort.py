def Insertion_Sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j],nums[j-1] = nums[j-1],nums[j]
            j-=1
            
    return nums
    
    
print(Insertion_Sort([5, 2, 9, 1, 5, 6])) # Output: [1, 2, 5, 5, 6, 9]