Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to update the value of an existing key.
a={1:2,3:4,5:6}
a.upddate({1:10})
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.upddate({1:10})
AttributeError: 'dict' object has no attribute 'upddate'. Did you mean: 'update'?
a.update({1:10})
a
{1: 10, 3: 4, 5: 6}
a[1]=20
a
{1: 20, 3: 4, 5: 6}
