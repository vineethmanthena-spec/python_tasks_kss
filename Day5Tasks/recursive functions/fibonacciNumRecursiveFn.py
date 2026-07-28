Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a recursive function to find the nth Fibonacci number.
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

    
print(fib(9))
34
