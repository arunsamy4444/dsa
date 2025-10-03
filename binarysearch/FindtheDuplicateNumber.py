def findDuplicate(nums):
    seen = set()
    for i in nums:
        if i not in seen:
            seen.add(i)
        else:
            print(i)

print(findDuplicate([1,3,4,2,2]))