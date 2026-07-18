Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program that prints numbers from 1 to 10 but skips even numbers using continue.
for num in range(1,11):
    if num%2==0:
        continue
    print(num)

    
1
3
5
7
9
