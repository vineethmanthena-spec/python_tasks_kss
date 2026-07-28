Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. Then using the math module, compute and display: 
#● Maximum value 
#● Minimum value 
#● Square root of the maximum number 
#● Logarithm of the minimum number
import math
import random
random_numbers=[random.randint(1,200)for _ in range(20)]
print(f"Generated List: {random_numbers}\n")
Generated List: [142, 30, 164, 35, 16, 113, 152, 55, 79, 10, 200, 180, 95, 33, 38, 6, 162, 140, 197, 86]

max_val = max(random_numbers)
print(f"Maximum value: {max_val}")
Maximum value: 200
min_val = min(random_numbers)
print(f"Minimum value: {min_val}")
Minimum value: 6
sqrt_max = math.sqrt(max_val)
print(f"Square root of the maximum number: {sqrt_max:.4f}")
Square root of the maximum number: 14.1421
log_min = math.log(min_val)
print(f"Natural logarithm of the minimum number: {log_min:.4f}")
Natural logarithm of the minimum number: 1.7918
