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