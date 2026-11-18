# Given an integer array, return true if it is sorted in ascending/non-decreasing order

'''
Pseudocode: (brute)
FUNCTION is_sorted(arr):
    FOR i from 0 to (size of arr - 1):
        FOR j from i+1 to (size of arr - 1):
            IF arr[i] > arr[j]:
                RETURN False
    RETURN True
'''

def is_sorted(numbers):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                return False
    return True

print(is_sorted([1, 2, 2, 3]))
print(is_sorted([5, 6, 0, -2]))

# Time: O(n*n), because every possible pair is compared in worst case ~ roughly n*n operations
# Space: O(1), because no additional space is used

'''
Pseudocode: (optimal)
FUNCTION is_sorted_v2(arr):
    FOR i from 1 to (size of arr - 1):
        IF arr[i] < arr[i-1]:
            RETURN False
    RETURN True
'''

def is_sorted_v2(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    return True

print(is_sorted([1, 2, 2, 3]))
print(is_sorted([5, 6, 0, -2]))

# Time: O(n), because the loop traverse from 2nd element of an array till the last element ~ roughly n operations
# Space: O(1), because no additional space is used