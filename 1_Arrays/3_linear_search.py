# Search an element in an array

'''
Pseudocode:
FUNCTION linear_search(arr, target):
    FOR i from 0 to size of arr:
        IF arr[i] is equals to target:
            RETURN i
    
    RETURN -1
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

print(linear_search([-9, 4, -2, 0, 12, 7], 0))

# Time: O(n), because the loop iterates the entire array element one-by-one
# Space: O(1), only using one loop variable (i) 