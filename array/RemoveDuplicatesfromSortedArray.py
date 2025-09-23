def remove_duplicates(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False

            
    
remove_duplicates([0,0,1,1,1,2,2,3,3,4])

# def remove_duplicates(nums):
#     a=list(set(nums))
#     print(a)

# remove_duplicates([0,0,1,1,1,2,2,3,3,4])


