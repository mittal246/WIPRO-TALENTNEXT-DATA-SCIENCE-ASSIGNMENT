#1. WAP to count the number of upper and lower case letters in a string.
s=input("Enter the string:")
upper = 0
lower = 0
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

#2. WAP that will check a given string is Palindrome or not.
s=input("Enter the string:")
if s==s[::-1]:
    print("Yes palindrome")
print("No not palindrome")

#3. Given a string,return a new string made of n copies of the first 2 chars of the orginial string where n is the length of the string.The string length will be >=2.
s=input("Enter the string:")
print(s[:2]*len(s))

#4. Given a string,if the fast or last character is 'x',return the string without those 'x' character,else return the string unchanged.
s=input("Enter the string:")
if s.startswith('x'):
        s = s[1:]
if s.endswith('x'):
        s = s[:-1]
print(s)

#5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.You may assume that n is the between 0 and the length of the string inclusive.
s=input("Enter the string:")
n=int(input("Enter the value of n:"))
print(s[-n:]*n)
 