def FindMinimuminRotatedSortedArray(arr):
    l=0
    r=len(arr)-1
    while l < r:
        m = (l+r)//2
        # if arr[m] <= arr[r]:
        #     r=m
        # else:
        #     l=m+1
            
        # if arr[m] > arr[r]:
        #     l=m+1
        # else:
        #     r=m
    print(arr[m])
    
# Test
print(FindMinimuminRotatedSortedArray([3,4,5,1,2]))      # 1
print(FindMinimuminRotatedSortedArray([4,5,6,7,0,1,2]))  # 0
print(FindMinimuminRotatedSortedArray([11,13,15,17]))    # 11