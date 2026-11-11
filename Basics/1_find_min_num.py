# Find min number in a given list/array

'''
Pseudocode:
FUNCTION find_min(list):
    IF list is empty:
        RETURN None
    SET max_value to the first item
    FOR EACH item in the list (starting from 2nd element):
        IF item < min_value:
            SET min_value to item
    RETURN min_value
'''

def find_min(numbers):
    # Edge case: If the list/array is empty
    if not numbers:
        return None 
    
    min_value = numbers[0]
    for number in numbers:
        if(number < min_value):
            min_value = number
    return min_value

print(find_min([45, 78, 0, 91, -5]))


# Time: O(n), because the loop traverse the entire list
# Space: O(1), only using 2 variables (min_value, number)