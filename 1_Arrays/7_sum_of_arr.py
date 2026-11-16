# Given an integer array, return the sum of all its elements

'''
Pseudocode:
FUNCTION sum_of_arr(arr):
    SET total to 0

    FOR i from 0 to the last element of the arr:
        SET total to total + i-th element of arr
    RETURN total
'''

def sum_of_arr(arr):
    total = 0

    for i in range(0, len(arr)):
        total += arr[i]
    return total

print(sum_of_arr([4, -2, 0, 7, -3]))

# Time: O(n), because the loop traverse the entire array
# Space: O(1), only using 2 variables (total, i)