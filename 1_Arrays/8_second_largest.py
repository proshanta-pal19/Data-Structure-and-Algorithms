# Given an integer array, find the second largest distinct element in the array

import math

'''
Pseudocode: (brute)
FUNCTION second_largest(arr):
    IF length of arr < 2: 
        RETURN None

    SET sorted_arr to sort of all array elements
    SET largest to last element of sorted_arr

    FOR i from (length of arr - 2) to 0:
        IF sorted_arr[i] < largest:
            RETURN sorted_arr[i]

    RETURN None
'''

def second_largest(numbers):
    if len(numbers) < 2:
        return None

    sorted_arr = sorted(numbers)
    largest = sorted_arr[-1]

    for i in range(len(numbers) - 2, -1, -1):
        if sorted_arr[i] < largest:
            return sorted_arr[i]

    return None

print(second_largest([7, 8, 4, 8, 5]))
print(second_largest([6, 6, 6]))
print(second_largest([6]))
print(second_largest([-5, -2, -9]))
print(second_largest([0, -1]))
print(second_largest([]))

# Time: O(nlogn), sorting the array requires n*logn times while backward iterations takes roughly n times. So, O(nlogn) + O(n) ~ O(nlogn)
# Space: O(n), because creating a new array to stored the sorted element of an array

'''
Pseudocode: (better)
FUNCTION second_largest_v2(arr):
    IF length of arr < 2:
        RETURN None
    
    SET largest to the first element of the arr
    SET secLargest to negative infinity

    FOR i from 1 to (size of arr - 1):
        IF arr[i] > largest:
            SET largest to arr[i]
    
    FOR EACH current in arr:
        IF current < largest AND current > secLargest:
            SET secLargest to current

    IF secLargest is still negative infinity:
        RETURN None
    RETURN secLargest
'''

def second_largest_v2(numbers):
    if len(numbers) < 2: 
        return None

    largest = numbers[0]
    secLargest = -math.inf

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    for current in numbers:
        if current < largest and current > secLargest :
            secLargest = current

    if secLargest == -math.inf:
        return None
    return secLargest

print(second_largest_v2([7, 8, 4, 8, 5]))
print(second_largest_v2([6, 6, 6]))
print(second_largest_v2([6]))
print(second_largest_v2([-5, -2, -9]))
print(second_largest_v2([0, -1]))
print(second_largest_v2([]))

# Time: O(n), because loop traverse twice (individually ~ roughly 2n times)
# Space: O(1), only using 2 variables (largest, secLargest) 

'''
Pseudocode: (optimal)
FUNCTION second_largest_v3(arr):
    IF length of arr < 2:
        RETURN None

    SET largest to the first element of the arr
    SET secLargest to negative infinity

    FOR i from 1 to (size of arr - 1):
        IF arr[i] > largest:
            SET secLargest to largest
            SET largest to arr[i]
        ELIF arr[i] < largest AND arr[i] > secLargest:
            SET secLargest to arr[i]
            
    IF secLargest is still negative infinity:
        RETURN None
    RETURN secLargest
'''

def second_largest_v3(numbers):
    if len(numbers) < 2:
        return None

    largest = numbers[0]
    secLargest = -math.inf

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            secLargest = largest
            largest = numbers[i]
        elif numbers[i] < largest and numbers[i] > secLargest:
            secLargest = numbers[i]

    if secLargest == -math.inf:
        return None
    return secLargest

print(second_largest_v3([7, 8, 4, 8, 5]))
print(second_largest_v3([6, 6, 6]))
print(second_largest_v3([6, 8, 8]))
print(second_largest_v3([6]))
print(second_largest_v3([-5, -2, -9]))
print(second_largest_v3([0, -1]))
print(second_largest_v3([5, -2, -1, 0, 7]))
print(second_largest_v3([]))

# Time: O(n), because loop traverse only once
# Space: O(1), using only 2 variables (largest, secLargest)
