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

#------ SOL 2 ----- 

# def ContainsDuplicate(arr):
#     if arr == []:
#         print('Empty')
#         return []
#     if len(arr) <=1:
#         print('Not enough elements to have duplicates')
#     arr2 = set(arr)
#     if len(arr2) != len(arr):
#         print('True')
#         return True
#     else:
#         print("No duplicates")
#         return False
    
    
    
# # Test
# print(ContainsDuplicate([1,2,3,1]))  # True
# print(ContainsDuplicate([1,2,3,4]))  # False
# print(ContainsDuplicate([]))         # False
# print(ContainsDuplicate([5]))        # False