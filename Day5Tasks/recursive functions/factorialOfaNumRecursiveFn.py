Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n<0:
        raise valueError("not defined")
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

number=6
print(factorial(number))
720
