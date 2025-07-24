#1. WAP to accept two numbers as command line arguments and display their sum.

import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum:", num1 + num2)

#2. WAP to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys

print("File Name:", sys.argv[0])
print("Welcome Message:", sys.argv[1])

#3. WAP to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = list(map(int, sys.argv[1:]))

if len(numbers) != 10:
    print("Please enter exactly 10 numbers.")
else:
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
