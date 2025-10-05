def rotate(nums, k):
    n = len(nums)
    k %= n  # normalize k in case k > n
    nums[:] = nums[-k:] + nums[:-k]  # rotate in-place

# Test
arr = [1,2,3,4,5,6,7]
rotate(arr, 3)
print(arr)  # Output: [5,6,7,1,2,3,4]
