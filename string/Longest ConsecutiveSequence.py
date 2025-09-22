def LongestConsecutiveSequence(nums):
    new_arr = sorted(set(nums))
    if not new_arr:
        return 0
    count=1
    l=1
    for i in range(1,len(new_arr)):
        if new_arr[i] - new_arr[i-1] == 1:
            count+=1
        else:
            count=1
        l = max(l,count)
    print(l)
    
print(LongestConsecutiveSequence([100,4,200,1,3,2])) #4 (1,2,3,4)


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         new_arr = sorted(set(nums))
#         if not new_arr:
#             return 0
#         count=1
#         long_count=1
#         for i in range(len(new_arr)-1):
#             if new_arr[i] == new_arr[i+1]-1:
#                 count+=1
#             else:
#                 count=1
#             long_count = max(long_count,count)
#         return long_count

        