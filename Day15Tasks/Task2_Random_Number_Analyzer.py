# Random Number Analyzer 
#Scenario: 
#A system generates random numbers for testing. 
#Task: 
#● Use random to generate 10 numbers 
#● Store in a list 
#● Use loop + condition to count even/odd numbers 
#● Use set to remove duplicates

import random
random_numbers = [random.randint(1, 50) for _ in range(10)]
print("Original List:", random_numbers)

even_count = 0
odd_count = 0

for num in random_numbers:
  if num % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")

unique_numbers = set(random_numbers)
print("Unique Numbers (Set):", unique_numbers)
