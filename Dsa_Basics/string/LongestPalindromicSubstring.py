def LongestPalindromicSubstring(s):
    
    if not s:
        return ''
    if len(s) == 1:
        return s
    longest = ""
    for i in range(len(s)):
        for j in range(i,len(s)):
            res = s[i:j+1]
            if res == res[::-1] and len(res) > len(longest):
                longest = res
    return longest


# Test
print(LongestPalindromicSubstring("babad"))  # "bab" or "aba"
print(LongestPalindromicSubstring("cbbd"))   # "bb"
