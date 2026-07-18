Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program using comparison operators.
a=15
b=10
c=15
print(f"is {a} = {b}? -> {a==b}")
is 15 = 10? -> False
print(f"is{a}={c} {a==c}
      
SyntaxError: unterminated string literal (detected at line 1)
print(f"is {a}={c}  {a==c}")
      
is 15=15  True
print(f"Is {a} greater than {b}? -> {a > b}")
      
Is 15 greater than 10? -> True
print(f"Is {b} less than {a}? -> {b < a}")
      
Is 10 less than 15? -> True
print(f"Is {a} greater than or equal to {c}? -> {a >= c}")
      
Is 15 greater than or equal to 15? -> True
print(f"Is {b} less than or equal to {a}? -> {b <= a}")
      
Is 10 less than or equal to 15? -> True
print(f"Is {b} between 5 and 20? -> {5 < b < 20}")
      
Is 10 between 5 and 20? -> True
