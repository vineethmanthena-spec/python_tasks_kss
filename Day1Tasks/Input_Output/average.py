Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Q: Write a program that takes three numbers as input and prints their average.
a=4
b=8
c=16
averge=a+b+c/3
print(average)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(average)
NameError: name 'average' is not defined. Did you mean: 'averge'?
print(averge)
17.333333333333332
average=a+b+c/3
print(average)
17.333333333333332
