def ValidAnagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    
# Test
print(ValidAnagram("anagram", "nagaram"))  # True
print(ValidAnagram("rat", "car"))          # False