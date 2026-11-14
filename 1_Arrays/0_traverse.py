# Traverse an array

'''
Pseudocode:
FUNCTION traverse(arr):
    FOR i from 0 to last position of arr:
        PRINT arr[i]
'''

def traverse(arr):
    for i in range(len(arr)):
        print(arr[i])

traverse([1, 5, 3, 9, 10, 13])

# Time: O(n), because the loop iterates the entire array
# Space: O(1), only using one loop variable (i)