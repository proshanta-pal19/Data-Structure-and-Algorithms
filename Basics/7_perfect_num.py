# Given an integer n, return true if n is a perfect number, otherwise return false

# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 

# Constraints: 1 <= n <= 10^8

'''
Pseudocode: (brute)
FUNCTION is_perfect_num_brute(n):
    IF n <= 1:
        RETURN False
    
    SET divisors_sum to 0
    FOR i from 1 to n:
        IF n % i == 0:
            SET divisors_sum as divisors_sum + i

    RETURN divisors_sum == n
'''

def perfect_num_brute(n: int) -> bool:
    if n <= 1:
        return False

    divisors_sum: int = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n

print(perfect_num_brute(6)) 
print(perfect_num_brute(36)) 
print(perfect_num_brute(28)) 
print(perfect_num_brute(496)) 
print(perfect_num_brute(1)) 
print(perfect_num_brute(8128)) 

# Time: O(n), because the loop traverse entire array except 1st element ~ roughly n steps
# Space: O(1), using only 1 variable (divisors_sum)


'''
Pseudocode: (optimal)
FUNCTION perfect_num_optimal(n):
    IF n <= 1:
        RETURN False
    
    SET divisors_sum to 1
    SET i to 2

    WHILE i*i <= n:
        IF n % i == 0:
            divisors_sum += i
            IF n // i != i:
                divisors_sum += (n // i)
        SET i to one step forward
    
    RETURN divisors_sum == n
'''

def perfect_num_optimal(n: int) -> bool:
    if n <= 1: 
        return False

    divisors_sum: int = 1
    i: int = 2

    while i*i <= n:
        if n % i == 0:
            divisors_sum += i
            if n // i != i:
                divisors_sum += (n // i)
        i += 1

    return divisors_sum == n

print(perfect_num_optimal(6)) 
print(perfect_num_optimal(36)) 
print(perfect_num_optimal(28)) 
print(perfect_num_optimal(496)) 
print(perfect_num_optimal(1)) 
print(perfect_num_optimal(8128)) 

# Time: O(sqrt(n)), because the loop runs upto the square root of the number
# Space: O(1), using only 1 variable (divisors_sum) 