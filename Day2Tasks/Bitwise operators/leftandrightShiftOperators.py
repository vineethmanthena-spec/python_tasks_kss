Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a program to perform left shift (<<) and right shift (>>) operations on a number
num=6
position=4
result=num<<position
print(f"left shift position is {num}<<{position}={result}")
left shift position is 6<<4=96
result2=num>>position
print(f"rightshift position is {num}>>{position}={result2}")
rightshift position is 6>>4=0
