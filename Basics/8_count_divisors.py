# Given a positive integer n, find the total count of its divisors

# A divisor is any positive integer that divides n completely, leaving a remainder of 0

# Constraints: 1<= n <= 1000

'''
Pseudocode: (brute)
FUNCTION count_divisors_brute(n):
    SET count to 0

    FOR i from 1 to n+1:
        IF n % i == 0:
            SET count to one step forward

    RETURN count 
'''

def count_divisors_brute(n: int) -> int:
    count: int = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    return count

print(count_divisors_brute(12))
print(count_divisors_brute(8))
print(count_divisors_brute(17))
print(count_divisors_brute(35))

# Time: O(n), because the loop traverse from 1 to n
# Space: O(1), only using one variable (count)


'''
Pseudocoe: (optimal)
FUNCTION count_divisors_optimal(n):
    SET count to 1
    SET i to 2
    
    WHILE i*i <= n:
        IF n % i == 0:
            SET count to one step forward
            IF n // i != i:
                SET count to one step forward
        SET i to one step forward  

    RETURN count
'''

def count_divisors_optimal(n: int) -> int:
    count: int = 0
    i: int = 1

    while i*i <= n:
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
        i += 1
    
    return count

print(count_divisors_optimal(12))
print(count_divisors_optimal(8))
print(count_divisors_optimal(17))
print(count_divisors_optimal(35))

# Time: O(sqrt(n)), because the loop runs upto the square root of the number
# Space: O(1), only using 2 variables (count, i)