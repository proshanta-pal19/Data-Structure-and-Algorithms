# Find min number in a given list/array

'''
Pseudocode:
FUNCTION find_min(numbers):
    IF numbers are empty:
        RETURN None
    min_value = first element of numbers
    FOR each number in numbers (starting from second element):
        IF number < min_value:
            min_value = number
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