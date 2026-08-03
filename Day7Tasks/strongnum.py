#Q:Write a program to check whether a given number is a Strong number.

def check_strong_number(num):
    original_num = num
    digit_sum = 0
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    while num > 0:
        digit = num % 10
        digit_sum += factorials[digit]
        num //= 10
        
    return digit_sum == original_num

user_input = int(input("Enter a number to check: "))

if check_strong_number(user_input):
    print(f"{user_input} is a Strong number.")
else:
    print(f"{user_input} is NOT a Strong number.")
