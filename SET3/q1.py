import random

# 1. Create a list of 10 random integers between 1 and 100
numbers = random.sample(range(1, 101), 10)
print("Original List:", numbers)

# a) Find the second largest and second smallest numbers
sorted_numbers = sorted(numbers)
second_largest = sorted_numbers[-2]
second_smallest = sorted_numbers[1]
print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)

# b) Separate the numbers into even and odd lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# c) Sort both lists in descending order
even_numbers.sort(reverse=True)
odd_numbers.sort(reverse=True)
print("Even Numbers (Descending):", even_numbers)
print("Odd Numbers (Descending):", odd_numbers)
