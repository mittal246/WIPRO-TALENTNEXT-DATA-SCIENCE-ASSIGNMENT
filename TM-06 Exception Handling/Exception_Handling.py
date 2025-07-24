#1. WAP to accept two numbers from the user and perform division.If any exception occurs,print an error message and else print the result.
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
else:
    print("Result of division:", result)

#2. WAP to accept a number from the user and check whether it is prime or not. If user enters anything other than number,handle the exception and print an error message.
try:
    num = int(input("Enter a number to check if it's prime: "))
    if num < 2:
        print("Not a prime number")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
except ValueError:
    print("Error: Please enter a valid integer.")

#3. WAP to accept the file name to be opened from the user ,if file exist print the contents of the file in title case or else handle the exception and print an error message.
try:
    filename = input("Enter file name to open: ")
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

#4. Declare a list with 10 integers and ask the user to enter an index.Check whether the number in that index is positive or the negaitve number.If any invalid index is entered handle the exception and print the error message.
numbers = [12, -5, 8, -22, 7, 0, 19, -3, 4, -10]

try:
    index = int(input("Enter index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print("The number at index", index, "is positive.")
    elif value < 0:
        print("The number at index", index, "is negative.")
    else:
        print("The number at index", index, "is zero.")
except IndexError:
    print("Error: Invalid index. Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")

