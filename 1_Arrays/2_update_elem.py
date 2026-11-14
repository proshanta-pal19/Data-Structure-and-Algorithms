# Updating array elements

'''
Pseudocode:
FUNCTION update_elem(arr, index, value):
    IF index < 0 OR index >= size of arr: (let, negative index is invalid)
        RETURN 'Invalid index'
    SET arr[index] to value
    RETURN arr
'''

def update_elem(arr, index, value):
    if index < 0 or index >= len(arr):
        return 'Invalid index'
    arr[index] = value
    return arr

print(update_elem([1, 2, 3, 4, 6], 4, 5))

# Time: O(1), as directly access the array and update in-place
# Space: O(1), as no extra space is used