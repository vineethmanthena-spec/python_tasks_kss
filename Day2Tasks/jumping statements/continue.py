Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program using continue to skip printing the number 3 in a loop from 1 to 10
for i in range(1,11):
    if i==3:
        continue
    print(i)

    
1
2
4
5
6
7
8
9
10
