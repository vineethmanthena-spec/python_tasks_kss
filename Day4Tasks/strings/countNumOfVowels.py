Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a program to count the number of vowels in a string.
text="hello  how are you?"
vowels="aeiouAEIOU"
count=0
for c in text:
    if c in vowels:
        count+=1

        
print(count)
7
