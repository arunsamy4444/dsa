#------ SOL 1 ----- 
def ContainsDuplicate(arr):
    d = {}
    for i in arr:
        if i in d:
            print('True - Dup found')
        d[i] = 1
    print('False')

     
# Test
print(ContainsDuplicate([1,2,3,4]))  # False