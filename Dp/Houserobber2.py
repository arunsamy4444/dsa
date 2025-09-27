def Houserobber2(nums):
    if len(nums) == 1:
        print(nums[0])
        
    def r2(arr):
        if len(arr) == 1:
            return arr[0]
        dp=[0]*len(arr)
        dp[0]=arr[0]
        dp[1]=max(arr[0],arr[1])
        for i in range(2,len(arr)):
            dp[i] = max(arr[i] + dp[i-2] , dp[i-1])
        return dp[-1]
    nums1 = nums[:-1]
    nums2 = nums[1:] 
    
    return max(r2(nums1), r2(nums2))
    

print(Houserobber2([1,2,3,1]))