Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Format a string using `format()` method.
text="hello, my name is {} and my age is {}."
reult=text.format("tony",8)
print(result)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined. Did you mean: 'reult'?
print(reult)
hello, my name is tony and my age is 8.
