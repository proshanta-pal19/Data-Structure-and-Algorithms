# Given a positive integer, check whether it is palindrome or not

'''
Pseudocode:
FUNCTION is_palindrome(number):
    IF number is negative:
        RETURN False

    SET rev to 0
    SET temp to original number

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
    IF number is negative:
        RETURN False

    SET s to number after converting it to string
    SET left to the first position
    SET right to the last position

    WHILE left < right:
        IF s[left] != s[right]:
            return False
        SET left to one step forward
        SET right to one step backward
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

'''
Pseudocode: (using string slicing)
FUNCTION is_palindrome_v3(number):
    IF number is negative:
        RETURN False

    SET s to number after converting it to string
    SET s to lowercase of s
    RETURN s == s[::-1]
'''

def is_palindrome_v3(n):
    if n < 0:
        return False
    
    s = str(n)
    s = s.lower()
    return s == s[::-1]

print(is_palindrome_v3(789))
print(is_palindrome_v3(-101))
print(is_palindrome_v3(10001))

# Time: O(n), because
# lower() method iterates each character ~ n characters
# [::-1] slicing for reverse copy each character ~ n characters
# compares each character of original and reversed ~ n comparison
# Total = n + n + n = 3n ~ O(n)

# Space: O(n), because 
# s.lower() and s[::-1] both creates a new string ~ roughly n characters
# Total: O(n)