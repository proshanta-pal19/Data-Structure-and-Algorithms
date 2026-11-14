# Accessing array elements

'''
Pseudocode:
FUNCTION access_elem(arr, index):
    IF index < 0 OR index >= size of arr: (let, negative index is invalid)
        RETURN 'Invalid index'
    RETURN arr[index]
'''

def access_elem(arr, index):
    if index < 0 or index >= len(arr):
        return 'Invalid index'
    return arr[index]

print(access_elem([10, -2, 5, 1, 15], 2))
print(access_elem([12, 5, 6, 9], -1))

# Time: O(1), as we access direct array element through it's index
# Space: O(1), as no extra space is used