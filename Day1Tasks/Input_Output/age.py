Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Q:Write a program that asks the user for their age and prints the age after 5 years.
age=input("please enter your age:)
          
SyntaxError: unterminated string literal (detected at line 1)
age=input("please enter your age:")
          
please enter your age:20
current_age=int(age)
          
future_age=current_age+5
          
print(future_age)
          
25
