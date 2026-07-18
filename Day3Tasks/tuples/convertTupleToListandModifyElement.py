Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(2,"hi",4,5,"hello",10)
type(t)
<class 'tuple'>
l=list(t)
type(l)
<class 'list'>
l[2]=6
print(l)
[2, 'hi', 6, 5, 'hello', 10]
u=tuple(l)
print(u)
(2, 'hi', 6, 5, 'hello', 10)
type(u)
<class 'tuple'>
