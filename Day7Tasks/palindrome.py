#Q:Write a program to check whether a number is a Palindrome.
def is_palindrome(num):
    if num < 0:
        return False
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
        
    return original == reversed_num

test_number = 12321
if is_palindrome(test_number):
    print(f"{test_number} is a palindrome number.")
else:
    print(f"{test_number} is not a palindrome number.")
