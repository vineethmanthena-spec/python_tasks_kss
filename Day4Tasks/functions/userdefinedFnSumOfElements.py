Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Q:. Write a function to find the sum of elements in a list using a user-defined function.
def find_list_sum(num):
    total_sum=0
    for number in num:
        total_sum += number
    return total_sum

l=[2,3,4,5,6,7]
result=find_list_sum(l)
print(result)
27
