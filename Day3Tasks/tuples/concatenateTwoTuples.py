Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q: Write a program to concatenate two tuples.
tuple1=(1,2,3)
tuple2=("a","b","c")
concatenate=(*tuple1,*tuple2)

print(concatenate)
(1, 2, 3, 'a', 'b', 'c')
