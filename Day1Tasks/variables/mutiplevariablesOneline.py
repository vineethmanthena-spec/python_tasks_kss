Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Q:Assign multiple values to multiple variables in one line.
x,y,z=3,"hi",5
pint(x,y,z)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pint(x,y,z)
NameError: name 'pint' is not defined. Did you mean: 'print'?
print(x)
3
print(y)
hi
print(z)
5
print(x,y,z)
3 hi 5
