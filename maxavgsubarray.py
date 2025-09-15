def max_avg_subarray(nums, k):
    l = 0
    r = k
    a = float('-inf')  # max sum found so far
    n = len(nums)
    while r <= n:
        sum=0
        for i in range(l,r):
            sum+=nums[i]
        if sum > a :
            a = sum
        l+=1
        r+=1
    print(a/k)
 
# Example
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(max_avg_subarray(nums, k))  # 12.75