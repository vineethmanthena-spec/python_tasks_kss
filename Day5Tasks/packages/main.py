from utilities  import math_operations
from utilities import string_operations

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

text=input("enter a string:")
print("addition=", math_operations.add(num1,num2))
print("multiplication=",math_operations.multiply(num1,num2))

print("uppercase=",string_operations.uppercase(text))
print("charactercount=",string_operations.char_count(text))

