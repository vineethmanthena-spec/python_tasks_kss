Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Create a sentence using two variables with formatting.
name="tony"
age=8
sentence=f"hello, my name is {}, my age is {}."
SyntaxError: f-string: empty expression not allowed
sentence=f"hello, my name is {name}, my age is {age}."
print(sentence)
hello, my name is tony, my age is 8.
