Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write an expression that calculates simple interest.
pricipal=5000
rate=2
time=3
simple_interest=(pricipal*rate*interest)/100
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    simple_interest=(pricipal*rate*interest)/100
NameError: name 'interest' is not defined
simple_interest=(pricipal*rate*time)/100
print(simple_interest)
300.0
