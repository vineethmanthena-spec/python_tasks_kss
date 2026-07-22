Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a function that returns the factorial of a number.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

print(factorial(5))
120
