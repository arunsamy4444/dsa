def ValidAnagram(s1,s2):
    d={}
    for i in s1:
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    # print(d)
    for j in s2:
        if j not in d:
            print('False')
        else:
            if d[j] == 1:
                del d[j]
            else:
                d[j]-=1
            
    if d == {}:
        print("True")
    else:
        print('False')

# print(ValidAnagram("anagram", "nagaram"))  # True
print(ValidAnagram("rat", "car"))          # False

    # if sorted(s1) == sorted(s2):
    #     return True
    # else:
    #     return False