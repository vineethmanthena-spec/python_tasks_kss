Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to find the length of a list.
num=[2,3,5,6,8,9]
length=leg(num)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    length=leg(num)
NameError: name 'leg' is not defined. Did you mean: 'len'?
length=len(num)
print(length)
6
