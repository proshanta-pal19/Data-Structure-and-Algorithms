# Given an array with distinct integers range between 0 to n. The array represents a permutation of the integers from 0 to n with one element missing. Find the missing element in the array.

'''
Pseudocode: (brute)
FUNCTION missing_num(arr):
    FOR i from 0 to size of arr:
        SET found to False
        FOR value from 0 to (size of arr - 1):
            IF value == i:
                SET found to True
                BREAK
        IF found is False:
            RETURN i
    RETURN -1
'''

def missing_num(numbers):
    for i in range(0, len(numbers)+1):
        found = False

        for value in numbers:
            if value == i:
                found = True
                break

        if not found:
            return i
    return -1

print(missing_num([3, 2, 0, 4]))
print(missing_num([3, 2, 4, 1]))
print(missing_num([0, 1]))
print(missing_num([0]))
print(missing_num([]))

# Time: O(n*n), because the outer loop runs for n elements from 0 and for each check the inner loop may runs all n array elements
# Space: O(1), only using 1 variable except loop variables (found)

'''
Pseudocode: (better)
FUNCTION missing_num_v2(arr):
    SORT the arr in-place in ASC order
    FOR i from 0 to (size of arr - 1):
        IF arr[i] != i:
            RETURN i
    RETURN size of arr
'''

def missing_num_v2(numbers):
    numbers.sort()

    for i in range(0, len(numbers)):
        if numbers[i] != i:
            return i

    return len(numbers)

print(missing_num_v2([3, 2, 0, 4]))
print(missing_num_v2([3, 2, 4, 1]))
print(missing_num_v2([0, 1]))
print(missing_num_v2([0]))
print(missing_num_v2([]))

# Time: O(nlogn), sorting the array requires n*logn operations, while iterating all array elements require n operations. So O(nlogn) + O(n) ~ O(nlogn)
# Space: O(1), because no extra space is used

'''
Pseudocode: (optimal)
FUNCTION missing_num_v3(arr):
    SET n to size of arr
    SET expected_sum to (n * (n+1)) / 2 
    SET actual_sum to 0

    FOR EACH value in arr:
        UPDATE actual_sum to actual_sum + value

    RETURN expected_sum -actual_sum 
'''

def missing_num_v3(numbers):
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for value in numbers:
        actual_sum += value

    return expected_sum - actual_sum

print(missing_num_v3([3, 2, 0, 4]))
print(missing_num_v3([3, 2, 4, 1]))
print(missing_num_v3([0, 1]))
print(missing_num_v3([0]))
print(missing_num_v3([]))

# Time: O(n), because the loop add all the elements of the array
# Space: O(1), only using 3 variables except loop variable (n, expected_sum, actual_sum)