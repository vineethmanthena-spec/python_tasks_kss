Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to reverse a list.
num=[2,3,5,6,8,9]
num.reverse()
print(num)
[9, 8, 6, 5, 3, 2]

num=[2,4,5,7,9]
rev_num=num[::-1]
print(rev_num)
[9, 7, 5, 4, 2]
