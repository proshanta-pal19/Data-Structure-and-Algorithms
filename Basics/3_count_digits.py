# Givan a positive integer, count how many digits present in it 

'''
Pseudocode:
FUNCTION count_digits(number):
    SET count as 0
    IF number is 0:
        RETURN 1
    WHILE(number > 0):
        SET count to count+1
        SET number to number/10 (integer)
    RETURN count
'''

def count_digits(n):
    count = 0

    # Edge case: If the number is 0
    if n == 0:
        return 1

    while(n > 0):
        count += 1
        n = n // 10
    return count

print(count_digits(1567))
print(count_digits(0))

# Time:  O(log_10 n), because one digit is removed in each iteration
# Space: O(1), only using 1 variable (count)