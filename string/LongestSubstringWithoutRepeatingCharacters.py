def lengthOfLongestSubstring(s):
    newArr = []
    max_len = 0
    for i in s:
        # print(i)
        if i not in newArr:
            newArr.append(i)
        else:
            idx = newArr.index(i)
            newArr = newArr[idx + 1:]
            newArr.append(i)
            
        max_len = max(max_len,len(newArr))
            
    print(max_len)
            
print(lengthOfLongestSubstring("abcabcbb"))  # 3



# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         stack = []
#         if s=="":
#             return 0
#         count = 0
#         for i in s:
#             if i not in stack:
#                 stack.append(i)
#             else:
#                 idx=stack.index(i)
#                 stack = stack[idx+1:]
#                 stack.append(i)
#             count = max(count,len(stack))
#         return count
 
        