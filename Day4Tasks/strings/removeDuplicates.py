Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to remove duplicate characters from a string.

def remove_dup(string):
    return"".join(dict.fromkeys(string))

text="aabbbccccdddddeeeeeeefff"
result=remove_dup(text)
print(result)
abcdef
