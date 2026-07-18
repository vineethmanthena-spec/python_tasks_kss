Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Display a floating number with 2 decimal places
num=3.45678
print(num:.2f)
SyntaxError: invalid decimal literal
print(f"{num:.2f}")
3.46
