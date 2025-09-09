class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int(''.join(map(str,digits)))
        nums+=1
        dl=[]
        for i in str(nums):
            dl.append(int(i))
        return dl

        