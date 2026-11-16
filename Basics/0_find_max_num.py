# Find max number in a given list/array

'''
Pseudocode: (brute)
FUNCTION find_max(arr):
    SET sorted_arr to sort of all array elements
    RETURN last element of sorted_arr
'''

def find_max(numbers):
    sorted_arr = sorted(numbers)
    return sorted_arr[-1]

print(find_max([5, 3, 9, -7, 2, 1]))

# Time: O(nlogn), sorting the array requires n*logn times
# Space: O(n), because creating a new array to stored the sorted element of an array

'''
Pseudocode: (optimal)
FUNCTION find_max_v2(arr):
    IF arr is empty:
        RETURN None

    SET max_value to the first item

    FOR EACH item in the arr (starting from 2nd element):
        IF item > max_value:
            SET max_value to item
    RETURN max_value
'''

def find_max_v2(numbers):
    # Edge case: If the list/array is empty
    if not numbers:
        return None 
    
    max_value = numbers[0]
    for number in numbers:
        if(number > max_value):
            max_value = number
    return max_value

print(find_max_v2([45, 78, 62, 91, 55]))

# Time: O(n), because the loop traverse the entire list
# Space: O(1), only using 2 variables (max_value, number)