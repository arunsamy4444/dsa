class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique=[]
        for num in nums:
            if num not in unique:
                unique.append(num)
        for i in range(len(unique)):
            nums[i]=unique[i]
        return len(unique)

        