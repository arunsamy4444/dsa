def longestConsecutive(nums):
    
    if not nums:
        return 0

    m_count = 1
    c_count = 1
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]-1:
            c_count +=1
        elif nums[i] == nums[i+1]:
            continue
        else:
            c_count=1
        m_count = max(c_count,m_count)
    return m_count
            
print(longestConsecutive([2,20,4,10,3,4,5])) #4