# Given an integer, determine whether it is an armstrong number or not

# An Armstrong number is a positive integer that is equal to the sum of its own digits, each raised to the power of the total number of digits in that number.

'''
Pseudocode:
FUNCTION is_armstrong(number):
    IF number is negative:
        RETURN False
    IF number is 0:
        RETURN True

    SET temp to the original number
    SET power to 0

    WHILE temp > 0:
        SET power to one step forward
        SET temp to temp/10 (integer)

    SET temp to the original number
    SET total to 0

    WHILE temp > 0:
        SET digit to temp % 10
        SET total to total + digit raised to the power 
        SET temp to temp/10 (integer)

    RETURN total == number
'''

def is_armstrong(n):
    if n < 0:
        return False
    if n == 0:
        return True

    temp = n
    power = 0

    while (temp > 0):
        power += 1
        temp = temp // 10

    temp = n
    total = 0

    while (temp > 0):
        digit = temp % 10
        total += digit ** power
        temp = temp // 10

    return total == n

print(is_armstrong(371))
print(is_armstrong(1675))

# Time: O(log_10 n), because the number is divided by 10 until it reaches 0 for each iteration 
# Space: O(1), only using 4 variables (temp, power, total, digit)