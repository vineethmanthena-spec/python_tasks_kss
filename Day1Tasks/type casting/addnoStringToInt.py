Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Add two numbers taken as strings by converting them to integers.
a="5"
b="10"
result=int(a=b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    result=int(a=b)
TypeError: 'a' is an invalid keyword argument for int()
result=int(a)+int(b)
print(result)
15
