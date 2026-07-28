Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a Python program using the math module to calculate and display the square root, floor value, and ceiling value of a number entered by the user.
import math
user_input = float(input("Enter a number: "))

Enter a number: 5
if user_input >= 0:
    square_root = math.sqrt(user_input)
    print(f"Square root of {user_input}: {square_root}")
else:
    print(f"Square root of {user_input}: Cannot calculate square root of a negative number using the standard math module.")

Square root of 5.0: 2.23606797749979
floor_value = math.floor(user_input)
print(f"Floor value of {user_input}: {floor_value}")
Floor value of 5.0: 5
ceil_value = math.ceil(user_input)
print(f"Ceiling value of {user_input}: {ceil_value}")
Ceiling value of 5.0: 5
