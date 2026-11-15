# Given an array, reverse it in place (without creating a new array)

'''
Pseudocode:
FUNCTION reverse_arr(arr):
    SET left to the first position
    SET right to the last position

    WHILE left < right:
        SWAP the item at left with the item at right 
        MOVE left one step forward
        MOVE right one step backward
    RETURN arr
'''

def reverse_arr(arr):
    left = 0
    right = len(arr) - 1

    while (left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_arr([1, 2, 3, 4, 5]))
print(reverse_arr([1, 2, 3, 4]))

# Time: O(n), as swapping n/2 times ~ roughly n times
# Space: O(1), only using 2 variables (left, right)