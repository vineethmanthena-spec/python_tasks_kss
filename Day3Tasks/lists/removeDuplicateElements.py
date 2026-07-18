Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to remove duplicate elements from a list.
num=[1,3,2,3,4,5,7]
unique_num=list(set(num))
print(unique_num)
[1, 2, 3, 4, 5, 7]
