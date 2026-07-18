Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:Write a program to find the sum of numbers from 1 to N using a loop
n=5
total_sum=0
for i in range(1,n+1):
    total_sum+=i

    
print(f"the sum of num from1 to {n} is:{tatal_sum}")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(f"the sum of num from1 to {n} is:{tatal_sum}")
NameError: name 'tatal_sum' is not defined. Did you mean: 'total_sum'?
print(f"te sum of num from 1 to {n} is: {total_sum}")
te sum of num from 1 to 5 is: 15
