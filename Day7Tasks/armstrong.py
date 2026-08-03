#Q:Write a program to check whether a given number is an Armstrong number or not.
def is_armstrong(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    

    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return armstrong_sum == number
try:
    user_input = int(input("Enter a positive integer: "))
    if user_input < 0:
        print("Please enter a positive integer.")
    elif is_armstrong(user_input):
        print(f"{user_input} is an Armstrong number.")
    else:
        print(f"{user_input} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
