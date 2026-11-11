# Find max number in a given list/array

'''
Pseudocode:
FUNCTION find_max(list):
    IF list is empty:
        RETURN None
    SET max_value to the first item
    FOR EACH item in the list (starting from 2nd element):
        IF item > max_value:
            SET max_value to item
    RETURN max_value
'''

def find_max(numbers):
    # Edge case: If the list/array is empty
    if not numbers:
        return None 
    
    max_value = numbers[0]
    for number in numbers:
        if(number > max_value):
            max_value = number
    return max_value

print(find_max([45, 78, 62, 91, 55]))


# Time: O(n), because the loop traverse the entire list
# Space: O(1), only using 2 variables (max_value, number)