# Find max number in a given list/array

'''
Pseudocode:
FUNCTION find_max(numbers):
    max_value = first element of numbers
    FOR each number in numbers (starting from second element):
        IF number > max_value:
            max_value = number
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