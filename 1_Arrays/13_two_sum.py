# Given an integer array and a target integer. Return the indices of two numbers that sum up to target. Exectly one answer exists, and you cannot use the same element twice. Return the answer in any order

# Constraints: 2 <= arr.length <= 10^4, -10^9 <= arr[i], target <= 10^9

'''
Pseudocode: (brute)
FUNCTION two_sum_brute(arr, target):
    SET n to length of the arr

    FOR i from 0 to n:
        FOR j from i+1 to n:
            IF arr[i] + arr[j] == target:
                RETURN [i, j]
    RETURN []
'''

from typing import List

def two_sum_brute(arr: List[int], target: int) -> List[int]:
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i, j]

    return []

print(two_sum_brute([4, 2, 6, 1, 10], 8))
print(two_sum_brute([1, 2, 4, 3, 4], 10))
print(two_sum_brute([5, 1, -3, 0, -9], -9))
print(two_sum_brute([0, 0, 0], 0))

# Time: O(n*n), because 2 nested loop goes through the entire array ~ roughly n*n steps
# Space: O(1), only using loop variable i, j which forgotten after checking each pair


'''
Pseudocode: (better) - sort with 2 pointers
FUNCTION two_sum_better(arr, target):
    SET pairs to pair of each element with its index
    SORT the pairs

    SET left to the first position of the arr
    SET right to the last position of the arr

    WHILE left < right:
        SET sum_of_elems to pairs[left][0] + pairs[right][0]

        IF sum_of_elems < target:
            SET left to one step forward
        IF sum_of_elems > target:
            SET right to one step backward
        ELSE:
            RETURN [pairs[left][1], pairs[right][1]]
    RETURN []
'''

def two_sum_better(arr: List[int], target: int) -> List[int]:
    pairs = [(elem, i) for i, elem in enumerate(arr)]
    pairs.sort()

    left = 0
    right = len(pairs) - 1

    while left < right:
        sum_of_elems = pairs[left][0] + pairs[right][0]

        if sum_of_elems < target:
            left += 1
        elif sum_of_elems > target:
            right -= 1
        else:
            return [pairs[left][1], pairs[right][1]]
    return []

print(two_sum_better([4, 2, 6, 1, 10], 8))
print(two_sum_better([1, 2, 4, 3, 4], 10))
print(two_sum_better([5, 1, -3, 0, -9], -9))
print(two_sum_better([0, 0, 0], 0))

# Time: O(n*nlogn), because sorting the value-index pairs requiring n*logn time
# Space: O(n), because one value-pair is stored for every array element ~ roughly n steps


'''
Pseudocode: (optimal) - hash map
FUNCTION two_sum_optimal(arr, target): 
    SET seen as an empty dictionary

    FOR i, value IN arr:
        SET partner to (target - value)

        IF partner IN seen:
            RETURN [seen[partner], i]
        
        SET seen[value] to i
    RETURN []
'''

def two_sum_optimal(arr: List[int], target: int) -> List[int]:
    seen = dict()

    for i, value in enumerate(arr):
        partner = target - value

        if partner in seen:
            return [seen[partner], i]

        seen[value] = i
    return []

print(two_sum_optimal([4, 2, 6, 1, 10], 8))
print(two_sum_optimal([1, 2, 4, 3, 4], 10))
print(two_sum_optimal([5, 1, -3, 0, -9], -9))
print(two_sum_optimal([0, 0, 0], 0))

# Time: O(n), because the loop traverse once ~ roughly n steps
# Space: O(n), the dictionary seen holds all elements in array before the pair is found in worst case 