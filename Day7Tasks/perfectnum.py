#Q:Write a program to check whether a number is a Perfect number.
def is_perfect_number(n):
    if n <= 1:
        return False
    divisor_sum =1
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_sum += i
            if i * i != n:
                divisor_sum += n // i
        i += 1

    return divisor_sum == n
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is NOT a Perfect Number.")
