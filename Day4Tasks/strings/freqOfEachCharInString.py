Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to count the frequency of each character in a string.
a="hello world"
freq={}
for c in a:
    if c in freq:
        freq[c] +=1
    else:
        freq[c]=1

        
print(freq)
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
