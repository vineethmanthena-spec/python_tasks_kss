Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to calculate the factorial of a number using a loop
num=5
factorial=1
if num<0:
    print("factorial does not exist for negative num")
elif num==0:
    print("the factorial is 1")
else:
    for i in range(1,n+1):
        factorial*=i

        
Traceback (most recent call last):
  File "<pyshell#10>", line 6, in <module>
    for i in range(1,n+1):
NameError: name 'n' is not defined
else:
    
SyntaxError: invalid syntax
for i in range(1,num+1):
    factorial*=i

    
print(f"the factorial of {num} is:{factorial}")
the factorial of 5 is:120
