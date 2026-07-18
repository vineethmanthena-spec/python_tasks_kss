Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Align text using formatting
text = "Python"
print(f"{texxt:>15}")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(f"{texxt:>15}")
NameError: name 'texxt' is not defined. Did you mean: 'text'?
print(f"{text:>15}")
         Python
print(f"{text:<15}")
Python         
print(f"{text:^15}")
    Python     
print(f"{text:-^15}")
----Python-----
print(text.center(15, '_')
      