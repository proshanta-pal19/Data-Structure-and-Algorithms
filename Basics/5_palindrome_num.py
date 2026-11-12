# Given a positive integer, check whether it is palindrome or not

'''
Pseudocode:
FUNCTION is_palindrome(number):
    IF number < 0:
        RETURN False

    SET rev to 0
    SET temp to number
    
    WHILE(temp > 0):
        SET lastdigit to temp%10
        SET rev to (rev * 10) + lastdigit
        SET temp to temp/10 (integer)

    RETURN number == rev
'''

def is_palindrome(n):
    if n < 0:
        return False

    rev = 0
    temp = n

    while(temp > 0):
        lastdigit = temp % 10
        rev = (rev * 10) + lastdigit
        temp = temp // 10

    return n == rev

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(9564))

# Time: O(log_10 n), because the number is divided by 10 until it reaches 0 for each iteration (number of steps = number of digits)
# Space: O(1), only using 3 variables (rev, temp, lastdigit)

'''
Pseudocode: (using two-pointer)
FUNCTION is_palindrome_v2(number):
    IF number < 0:
        RETURN False

    SET s to number after converting to string
    SET left to 0
    SET right to last index of the number

    WHILE left < right:
        IF s[left] != s[right]:
            return False
        SET left to left+1
        SET right to right-1
    RETURN True
'''

def is_palindrome_v2(n):
    if n < 0:
        return False
    
    s = str(n)
    left = 0
    right = len(s) - 1

    while (left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome_v2(1001))
print(is_palindrome_v2(101))
print(is_palindrome_v2(-11))