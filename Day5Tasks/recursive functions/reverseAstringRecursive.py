Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a recursive function to reverse a string.
def reverse_string(txt):
    if len(txt)<=1:
        return txt
    return reverse_string(txt[1:])+txt[0]

text="hello"
print(reverse_string(text))
olleh

