# Given an integer array, return True if any value appears at least twice.

'''
Pseudocode: (brute)
FUNCTION contains_duplicate(arr):
    FOR i from 0 to (size of arr - 1):
        FOR j from i+1 to (size of arr - 1):
            IF arr[i] == arr[j]:
                RETURN True
    RETURN False
'''

def contains_duplicate(numbers):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False

print(contains_duplicate([2, 4, 5, 4, 1]))
print(contains_duplicate([8, 3, 10, 7]))
print(contains_duplicate([1, 0, -1, 0]))
print(contains_duplicate([3, 0, -5, 5]))
print(contains_duplicate([-3, -7, -5, -7]))
print(contains_duplicate([5]))
print(contains_duplicate([]))

# Time: O(n*n), because 2 nested loops goes through the entire array ~ roughly n*n operations
# Space: O(1), only using loop variable i which forgotten after checking each pair

'''
Pseudocode: (better)
FUNCTION contains_duplicate_v2(arr):
    SORT the arr elements

    FOR i from 1 to (size of arr - 1):
        IF arr[i] == arr[i-1]:
            RETURN True
    RETURN False
'''

def contains_duplicate_v2(numbers):
    numbers.sort()

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            return True
    return False

print(contains_duplicate_v2([2, 4, 5, 4, 1]))
print(contains_duplicate_v2([8, 3, 10, 7]))
print(contains_duplicate_v2([1, 0, -1, 0]))
print(contains_duplicate_v2([3, 0, -5, 5]))
print(contains_duplicate_v2([-3, -7, -5, -7]))
print(contains_duplicate_v2([5]))
print(contains_duplicate_v2([]))

# Time: O(n*logn), because sorts the array takes n*logn steps
# Space: O(1), sort() function sorted in place, so no copy is made.