# Given an integer array, find the second largest distinct element in the array

import math
from typing import List

'''
Pseudocode: (brute)
FUNCTION second_largest_brute(arr):
    IF length of arr < 2: 
        RETURN -1

    SET sorted_arr to sort of all array elements
    SET largest to last element of sorted_arr

    FOR i from (length of arr - 2) to 0:
        IF sorted_arr[i] < largest:
            RETURN sorted_arr[i]

    RETURN -1
'''

def second_largest_brute(arr: List[int]) -> int:
    if len(arr) < 2:
        return -1

    sorted_arr: List[int] = sorted(arr)
    largest: int = sorted_arr[-1]

    for i in range(len(arr) - 2, -1, -1):
        if sorted_arr[i] < largest:
            return sorted_arr[i]

    return -1

print(second_largest_brute([7, 8, 4, 8, 5]))
print(second_largest_brute([6, 6, 6]))
print(second_largest_brute([6]))
print(second_largest_brute([-5, -2, -9]))
print(second_largest_brute([0, -1]))
print(second_largest_brute([]))

# Time: O(nlogn), sorting the array requires n*logn operations while backward iterations takes roughly n operations. So, O(nlogn) + O(n) ~ O(nlogn)
# Space: O(n), because creating a new array to stored the sorted element of an array


'''
Pseudocode: (better)
FUNCTION second_largest_better(arr):
    IF length of arr < 2:
        RETURN -1
    
    SET largest to the first element of the arr
    SET secLargest to negative infinity

    FOR i from 1 to (size of arr - 1):
        IF arr[i] > largest:
            SET largest to arr[i]
    
    FOR EACH current in arr:
        IF current < largest AND current > secLargest:
            SET secLargest to current

    IF secLargest is still negative infinity:
        RETURN -1
    RETURN secLargest
'''

def second_largest_better(arr: List[int]) -> int:
    if len(arr) < 2: 
        return -1

    largest: int = arr[0]
    secLargest: int = -math.inf

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for current in arr:
        if current < largest and current > secLargest :
            secLargest = current

    if secLargest == -math.inf:
        return -1
    return secLargest

print(second_largest_better([7, 8, 4, 8, 5]))
print(second_largest_better([6, 6, 6]))
print(second_largest_better([6]))
print(second_largest_better([-5, -2, -9]))
print(second_largest_better([0, -1]))
print(second_largest_better([]))

# Time: O(n), because loop traverse twice (individually ~ roughly 2n times)
# Space: O(1), only using 2 variables (largest, secLargest) 


'''
Pseudocode: (optimal)
FUNCTION second_largest_optimal(arr):
    IF length of arr < 2:
        RETURN -1

    SET largest to the first element of the arr
    SET secLargest to negative infinity

    FOR i from 1 to (size of arr - 1):
        IF arr[i] > largest:
            SET secLargest to largest
            SET largest to arr[i]
        ELIF arr[i] < largest AND arr[i] > secLargest:
            SET secLargest to arr[i]
            
    IF secLargest is still negative infinity:
        RETURN -1
    RETURN secLargest
'''

def second_largest_optimal(arr: List[int]) -> int:
    if len(arr) < 2:
        return -1

    largest: int = arr[0]
    secLargest: int = -math.inf

    for i in range(1, len(arr)):
        if arr[i] > largest:
            secLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secLargest:
            secLargest = arr[i]

    if secLargest == -math.inf:
        return -1
    return secLargest

print(second_largest_optimal([7, 8, 4, 8, 5]))
print(second_largest_optimal([6, 6, 6]))
print(second_largest_optimal([6, 8, 8]))
print(second_largest_optimal([6]))
print(second_largest_optimal([-5, -2, -9]))
print(second_largest_optimal([0, -1]))
print(second_largest_optimal([5, -2, -1, 0, 7]))
print(second_largest_optimal([]))

# Time: O(n), because loop traverse only once
# Space: O(1), using only 2 variables (largest, secLargest)