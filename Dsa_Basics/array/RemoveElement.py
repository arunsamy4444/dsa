def RemoveElement(arr,val):
    p=0
    for i in range(len(arr)):
        if arr[i] == val:
            continue
        else:
            arr[p] = arr[i]
            p+=1
    print(p)
  
print(RemoveElement([3, 2, 2, 3],3))