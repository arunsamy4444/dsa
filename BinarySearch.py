def BinarySearch(arr , tar):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r)//2
        if arr[m] == tar :
            return m
        elif arr[m] < tar:
            l = m+1
        elif arr[m] > tar:
            r = m-1
    return -1
    
    
print(BinarySearch([-1,0,3,5,9,12] , 98)) 
print(BinarySearch([-1,0,3,5,9,12] , 9))