def TwoSum(arr,tar):
    
    if arr == []:
        print('Empty bro')
        return []
    if len(arr) == 1:
        print('Not enough numbers')
        return []
    
    for i in range(0,len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i]+ arr[j] == tar:
                return [arr[i], arr[j]]
    return []
                
                   
print(TwoSum([2, 7, 11, 15], 9))   # Output: [2, 7]
print(TwoSum([3, 2, 4], 6))        # Output: [2, 4]
print(TwoSum([3, 3], 6))           # Output: [3, 3]
print(TwoSum([1, 2], 3))           # Output: [1, 2]
