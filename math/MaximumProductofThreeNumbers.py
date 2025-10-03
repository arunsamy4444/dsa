def MaximumProductofThreeNumbers(nums):
    nums.sort()
    res1 = nums[-1]*nums[-2]*nums[-3]
    res2 = nums[0]*nums[1]*nums[-1]
    return max(res1,res2)
   
print(MaximumProductofThreeNumbers([1, 2, 3, 4,0])) #24