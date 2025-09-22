def TwoSum(arr,tar):
    
    if arr == []:
        print('Empty bro')
        return []
    if len(arr) == 1:
        print('Not enough numbers')
        return []
    
    for i in range(0,len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i]+ arr[j] == tar:
                return [arr[i], arr[j]]
    return []
                
                   
# print(TwoSum([2, 7, 11, 15], 9))   # Output: [2, 7]
# print(TwoSum([3, 2, 4], 6))        # Output: [2, 4]
# print(TwoSum([3, 3], 6))           # Output: [3, 3]
# print(TwoSum([1, 2], 3))           # Output: [1, 2]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d={}
#         if len(nums)<2:
#             return -1
#         for i,num in enumerate(nums):
#             complement = target - num
#             if complement in d:
#                 return [d[complement],i]
#             else:
#                 d[num]=i
#         return -1

        # if len(nums)<2:
        #     return -1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]== target:
        #             return [i,j]
        # else:
        #     return -1

 
        
        




        
