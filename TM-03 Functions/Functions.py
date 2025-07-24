# 1. Write a function to return the sum of all numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20
def sum_of_list(numbers):
    return sum(numbers)

print(sum_of_list([8, 2, 3, 0, 7]))


# 2. Write a function to return the reverse of a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"
def reverse_string(s):
    return s[::-1]

print(reverse_string("1234abcd"))

# 3. Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  

# 4. Write a function that accepts a string and prints the number of uppercase and lowercase letters in it.
def count_case_letters(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_case_letters("HelloWorld123")

# 5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  

