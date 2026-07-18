Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program that searches for a number in a list and breaks the loop when found.
list=[2,4,5,7,10,15]
req_num=7
for i in list:
    print(f"checking num:{i}")
    if i==req_num:
        print(f"found {req_num}")
        break

    
checking num:2
checking num:4
checking num:5
checking num:7
found 7
