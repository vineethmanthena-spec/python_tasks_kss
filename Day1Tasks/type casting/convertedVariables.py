Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to display the type of converted variable
string_num="45"
int_num=100
float_num=23.75
convert_to_int=int(string_num)
convert_to_float=float(int_num)
convert_to_string=str(float_num)
print(f"value:{convert_to_int}|new type:{type(convert_to_int)}")
value:45|new type:<class 'int'>
print(f"value:{convert_to_float}|new type:{typt(convert_to_float)}")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(f"value:{convert_to_float}|new type:{typt(convert_to_float)}")
NameError: name 'typt' is not defined. Did you mean: 'type'?
print(f"value:{convert_to_float}|new type:{type(convert_to_float)}")
value:100.0|new type:<class 'float'>
print(f"value:{convert_to_string}|new type:{type(convert_to_string)}")
value:23.75|new type:<class 'str'>
