def findMaxConsecutiveOnes(nums):
    max_count = 0
    cur_count = 0
    for i in nums:
        if i == 1:
            cur_count+=1
            max_count=max(max_count,cur_count)
        else:
            cur_count=0
    return max_count
    
    
print(findMaxConsecutiveOnes([1,1,0,1,1,1])) #3