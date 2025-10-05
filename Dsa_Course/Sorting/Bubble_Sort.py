def bubble_sort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
    return arr  
    
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))