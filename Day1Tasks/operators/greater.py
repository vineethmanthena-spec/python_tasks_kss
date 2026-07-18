Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to check if one number is greater than another.
a=foat(input("enter the num:"))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=foat(input("enter the num:"))
NameError: name 'foat' is not defined. Did you mean: 'float'?
a=float(input("enter the num:"))
enter the num:50
b=float(input("enter the num:"))
enter the num:40
if a>b:
    print(f"{a} is greater than {b})
          
SyntaxError: unterminated string literal (detected at line 2)
if a>b:
          print (f"{a} is greatr than {b}")

          
50.0 is greatr than 40.0
