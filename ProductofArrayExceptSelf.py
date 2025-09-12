def ProductofArrayExceptSelf(arr):
    final = [1]*len(arr)
    # print(final)
    prefix = 1
    for i in range(len(arr)):
        # print(arr[i])
        final[i] = prefix
        prefix*=arr[i]
        # print(final)
    suffix = 1
    for i in range(len(arr)-1,-1,-1):
        final[i] *=suffix
        
        suffix *=arr[i]
    print(final)
        
#just copied .... 
    
print(ProductofArrayExceptSelf([1,2,3,4]))