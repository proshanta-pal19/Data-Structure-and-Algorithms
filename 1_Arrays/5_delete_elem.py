# Delete an element at a particular index in an array

'''
Pseudocode:
FUNCTION delete_elem(arr, index):
    FOR EACH position i, from index up to (second last position):
        COPY the item at position (i+1) into position i
    REMOVE the last position
    RETURN arr
'''

from typing import List

def delete_elem(arr: List[int], index: int) -> List[int]:
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr

print(delete_elem([10, 20, 25, 30, 40], 1))

# Time: O(n), because every existing element must shift to the left ~ roughly n times
# Space: O(1), only using one loop variable (i)