Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write an expression using parentheses to change precedence.
a=2
b=4
c=6
r=(a+b)*c #parenthesses
print(r)
36
r=a+b*c #without paranthesses
print(r)
26
