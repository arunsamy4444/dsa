def ValidPalindrome(s):
    res = ''.join(c.lower() for c in s if c.isalnum())
    if not res :
        return False
    if res == res[::-1]:
        print('Its a Plaindorme str')
        return True
    else:
        print("Not a Palindrome string")
        return False    

print(ValidPalindrome("A man, a plan, a canal: Panama"))
print(ValidPalindrome("race a car"))