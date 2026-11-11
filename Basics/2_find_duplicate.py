# Given a list/array, determine any element appears more than once

'''
Pseudocode:
FUNCTION has_duplicate(list):
    SET n to the length of numbers 
    FOR i from 0 to n-1:
        FOR j from i+1 to n-1:
            IF list[i] == list[j]
                RETURN True
    RETURN False

For example, [1, 3, 1, 8, 10]
Index:        0  1  2  3  4 
'''

def has_duplicate(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] == numbers[j]:
                return True
    return False


print(has_duplicate([1, 3, 1, 8, 10]))
print(has_duplicate([9, -3, 1, 0, -6]))


# Time: O(n*n)
# Let, n = 5; [1, 3, 1, 8, 10]
# i = 0 | j = 1, 2, 3, 4 | 4 comparison
# i = 1 | j = 2, 3, 4    | 3 comparison
# i = 2 | j = 3, 4       | 2 comparison
# i = 3 | j = 4          | 1 comparison
# Total = 4 + 3 + 2 + 1 = 10
# Genearal Solution = n*(n-1)/2 ~ n*n

# Space: O(1), only using 3 variables (n, i, j)

'''
Pseudocode: (using built-in set)
FUNCTION has_duplicate_v2(list):
    SET seen as an empty set
    FOR i from 0 to n-1:
        IF i in seen:
            RETURN True
        ADD i to seen
    RETURN False
'''

def has_duplicate_v2(numbers):
    seen = set()
    for i in numbers:
        if i in seen:
            return True
        seen.add(i)
    return False


# Time: O(n), because loop traverse the entire list n times 
# Space: O(n), because we store the n number of elements in a set