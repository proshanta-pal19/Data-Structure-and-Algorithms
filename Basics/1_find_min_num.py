# Find min number in a given list/array

'''
Pseudocode: (brute)
FUNCTION find_min(arr):
    SET sorted_arr to sort of all array elements
    RETURN first element of sorted_arr
'''

def find_min(numbers):
    sorted_arr = sorted(numbers)
    return sorted_arr[0]

print(find_min([7, 0, 9, -7, 2, 10]))

# Time: O(nlogn), sorting the array requires n*logn times
# Space: O(n), because creating a new array to stored the sorted element of an array

'''
Pseudocode: (optimal)
FUNCTION find_min_v2(list):
    IF list is empty:
        RETURN None
    SET max_value to the first item
    FOR EACH item in the list (starting from 2nd element):
        IF item < min_value:
            SET min_value to item
    RETURN min_value
'''

def find_min_v2(numbers):
    # Edge case: If the list/array is empty
    if not numbers:
        return None 
    
    min_value = numbers[0]
    for number in numbers:
        if(number < min_value):
            min_value = number
    return min_value

print(find_min_v2([45, 78, 0, 91, -5]))

# Time: O(n), because the loop traverse the entire list
# Space: O(1), only using 2 variables (min_value, number)