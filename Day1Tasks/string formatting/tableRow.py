Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:. Print a table row using formatted strings
name="tony"
role= "dev"
id = 101
print(f"{name:<15} | {role:<15} | {id<5}")
tony            | dev             | False
print(f"{name:<6}|{role:<6|{id:<5}")
SyntaxError: f-string: expecting '}'
print(f"{name:<6}|{role:<6}|{id:<6}")
tony  |dev   |101   
