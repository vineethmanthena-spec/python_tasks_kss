Python 3.10.0 (t,ags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a recursive function to calculate the sum of digits of a number.
def sum_of_digits(n):
    n=abs(n)
    if n<10:
        return n
    return (n%10)+sum_of_digits(n//10)

number=12345
print(number)
12345
print(sum_of_digits(number))
15
number=3456
print(sum_of_digits(number))

