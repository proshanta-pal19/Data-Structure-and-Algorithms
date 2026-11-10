# Given a list/array, determine any element appears more than once

'''
Pseudocode:
FUNCTION has_duplicate(numbers):
    n = length of numbers 
    FOR i = 0 to i = n-1:
        FOR j = i+1 to j = n-1:
            IF numbers[i] == numbers[j]
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