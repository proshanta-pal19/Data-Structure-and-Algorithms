# Insert a value at a particular index in an array

'''
Pseudocode:
FUNCTION insert_elem(arr, index, value):
    ADD an empty slot at the end of the list/array
    FOR EACH position i, from the last position down to (index + 1):
        COPY the item at position (i-1) into position i
    SET arr[index] to value
    RETURN arr
'''

from typing import List

def insert_elem(arr: List[int], index: int, value: int) -> List[int] :
    arr.append(-1)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i-1]
    arr[index] = value
    return arr

print(insert_elem([10, 20, 30, 40], 2, 25))

# Time: O(n), because every existing element must shift to the right ~ roughly n times
# Space: O(1), only using one loop variable (i)