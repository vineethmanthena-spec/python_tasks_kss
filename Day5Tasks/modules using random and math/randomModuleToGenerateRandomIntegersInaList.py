Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a Python program using the random module to generate 10 random integersbetween 1 and 100 and store them in a list. Print the list.
import random
r_num=[random.randint(1,100) for _ in range(10)]
print(r_num)
[93, 95, 85, 86, 57, 41, 98, 78, 21, 98]
