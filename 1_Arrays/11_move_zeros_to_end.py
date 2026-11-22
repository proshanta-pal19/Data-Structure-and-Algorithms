# Given an integer array, move all 0's to the end of the array while keeping the order of non-zero elements. Do it in-place. 

'''
Pseudocode: (brute)
FUNCTION move_zeroes(arr):
    SET new_arr to empty array

    FOR EACH value IN arr:
        IF value != 0:
            APPEND value to new_arr

    SET zero_count to size of arr - size of new_arr
    
    REPEAT zero_count times:
        APPEND 0 to new_arr

    FOR i from 0 to (size of arr - 1):
        SET arr[i] to new_arr[i]
    
    RETURN arr
'''

def move_zeroes(numbers):
    new_arr = []

    for value in numbers:
        if value != 0:
            new_arr.append(value) 

    zero_count = len(numbers) - len(new_arr)  

    for _ in range(zero_count):             
        new_arr.append(0)

    for i in range(len(numbers)):
        numbers[i] = new_arr[i]   

    return numbers          

print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([4, -6, 0, 1, 5]))
print(move_zeroes([0, 1, 0]))
print(move_zeroes([0, 0, 0]))
print(move_zeroes([1, 0, -1]))
print(move_zeroes([]))

# Time: O(n), because 
# The 1st loop traverse the entire array to append non-zero elements ~ take n operations
# The 2nd loop traverse how many zero on the array ~ rougly n operations
# The 3rd loop traverse the entire array to change the original array ~ n operations
# So, n + n + n = 3n ~ O(n)

# Space: O(n), because we're using an array to store the elements

'''
Pseudocode: (better)
FUNCTION move_zeroes_v2(arr):
    SET pos to 0

    FOR i from 0 to (size of arr - 1):
        IF arr[i] != 0:
            arr[pos] = arr[i]
            SET pos to one step forward  
    
    FOR i from pos to (size of arr -1):
        arr[i] = 0
    
    RETURN arr
'''

def move_zeroes_v2(numbers):
    pos = 0

    for i in range(0, len(numbers)):
        if numbers[i] != 0:
            numbers[pos] = numbers[i]
            pos += 1

    for i in range(pos, len(numbers)):
        numbers[i] = 0

    return numbers
    
print(move_zeroes_v2([0, 1, 0, 3, 12]))
print(move_zeroes_v2([4, -6, 0, 1, 5]))
print(move_zeroes_v2([0, 1, 0]))
print(move_zeroes_v2([0, 0, 0]))
print(move_zeroes_v2([1, 0, -1]))
print(move_zeroes_v2([]))

# Time: O(n), because the 1st traversal places non-zero values and 2nd traversal fills the remaining positions with 0's
# Space: O(1), because the array is modified in-place using pos variable, no extra array is used here