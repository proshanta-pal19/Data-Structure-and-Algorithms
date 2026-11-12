# Given an integer (both positive and negative), reverse it's digits

'''
Pseudocode:
FUNCTION reverse_num(number):
    SET rev to 0
    SET isNeg to number < 0

    IF isNeg:
        SET number to absolute value of number 

    WHILE(n > 0):
        SET lastdigit to number%10
        SET rev to (rev * 10) + lastdigit
        SET number to number/10 (integer)

    IF isNeg:
        RETURN -rev
    RETURN rev
'''

def reverse_num(n):
    rev = 0
    isNeg = n < 0

    if isNeg:
        n = abs(n)

    while(n > 0):
        lastdigit = n%10
        rev = (rev * 10) + lastdigit
        n = n // 10

    if isNeg:
        return -rev
    return rev

print(reverse_num(1234))
print(reverse_num(1200))
print(reverse_num(-1200))

# Time: O(log_10 n), because the number is divided by 10 until it reaches 0 for each iteration (number of steps = number of digits)
# Space: O(1), only using 3 variables (rev, isNeg, lastdigit)