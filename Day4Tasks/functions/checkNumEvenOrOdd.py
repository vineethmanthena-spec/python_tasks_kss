Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a function to check whether a number is even or odd.
def check(num):
    if num %2==0:
        return "even"
    else:
        return "odd"

    
print(check(10))
even
print(check(7))
odd
