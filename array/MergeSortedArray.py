def merge(nums1, m, nums2, n):
    res = nums1[:m] + nums2[:n]
    print(nums1[:m])
    print(nums2[:n])
    res.sort()
    print(res)

# Test
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)

    
