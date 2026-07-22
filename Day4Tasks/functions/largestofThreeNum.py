Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:. Write a Python program with a function that returns the largest of three numbers.
def find_largest_builtin(num1, num2, num3):
    return max(num1, num2, num3)

a=5
b=9
c=3
r=find_larest_builtin(a,b,c)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    r=find_larest_builtin(a,b,c)
NameError: name 'find_larest_builtin' is not defined. Did you mean: 'find_largest_builtin'?
r=find_largest_builtin(a,b,c)
print(r)
9
