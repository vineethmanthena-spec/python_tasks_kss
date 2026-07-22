Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:. Write a function that takes a string as input and returns the number of vowels.
def count_vowels(text):
    vowels="aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

r=count_vowels("vineeth")
print(r)
3
