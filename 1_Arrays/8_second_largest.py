# Given an integer array, find the second largest distinct element in the array

'''
Pseudocode: (brute)
FUNCTION second_largest(arr):
    IF length of arr < 2: 
        RETURN -1

    SET sorted_arr to sort of all array elements
    SET largest to last element of sorted_arr

    FOR i from (length of arr - 2) to 0:
        IF sorted_arr[i] < largest:
            RETURN sorted_arr[i]

    RETURN -1
'''

def second_largest(numbers):
    if len(numbers) < 2:
        return -1

    sorted_arr = sorted(numbers)
    largest = sorted_arr[-1]

    for i in range(len(numbers) - 2, -1, -1):
        if sorted_arr[i] < largest:
            return sorted_arr[i]

    return -1

print(second_largest([7, 8, 4, 8, 5]))
print(second_largest([6, 6, 6]))
print(second_largest([6]))

# Time: O(nlogn), sorting the array requires n*logn times while backward iterations takes roughly n times. So, O(nlogn) + O(n) ~ O(nlogn)
# Space: O(n), because creating a new array to stored the sorted element of an array