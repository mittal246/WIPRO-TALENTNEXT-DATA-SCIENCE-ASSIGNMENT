# Q1. Write a program to check if a given number is Positive, Negative or Zero.
num=int(input("Enter the number you want to check: "))
if num<0:
    print("Negative")
elif num>0:
    print("Positive")
else:
    print("Neutral")
    
# Q2. Write a program to check if a given number is odd or even.
num=int(input("Enter the number:"))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# Q3.  Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num,rem=0,0
if num<0 or num2<0:
    print("Invalid numbers entered. ")
else:
    num=num%10
    rem=num%10
    if num==rem:
        print("True")
    else:
        print("False")

# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11):
    print(i,end=" ")

# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23,58):
    if i%2==0:
        print(i)

# Q6. Write a program to check if a given number is prime or not.
import math
num = int(input("Enter the number to be checked: "))
if num < 2:
    print("Not a prime number")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# Q7. Write a program to print prime numbers between 10 and 99.
for num in range(10,100):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ") 

# Q8. Write a program to print the sum of all the digits of a given number.
num=int(input("Enter the number:"))
sum_of_digits=0
last_digit=0
while num>0:
    last_digit=num%10
    sum_of_digits+=last_digit
    num=num//10
print(sum_of_digits)

# Q9. Write a program to reverse a given number and print.
num=int(input("Enter the number:"))
rem,rev=0,0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)

# Q10. Write a program to find if the given number is palindrom or not.
num=int(input("Enter the number:"))
rem,rev=0,0
temp=num
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if temp==rev:
    print("Palindrome")
else:
    print("Not palindrome")
