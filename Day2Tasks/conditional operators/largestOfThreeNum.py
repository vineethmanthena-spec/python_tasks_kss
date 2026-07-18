Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to find the largest of three numbers using if-elif-else
a=2
b=4
c=6
if (a>=b)and(a>=c):
    largest=a
elif (b>=a)and(b>=c):
    largest=b
else:
    largest=c

    

print(f"The largest number is : {largest}")
The largest number is : 6
