class Solution:
    def merge(self, nums1, m, nums2, n):
        res = nums1[:m]+ nums2[:n]
        res.sort()
        for i in range(len(res)):
            nums1[i] = res[i]