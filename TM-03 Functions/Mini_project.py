'''
1. Write a Python function that accepts a hyphen-separated of colors as input and returns the colors in a hyphen-separated sequence after sort them alphabetically.
Constraint:- All colors will be completely in either lower case or upper case.
Sample Input 1:- green-red-yellow-black-white
Sample Output 1:- black-green-red-white-yellow

'''
def sort_colors(color_string):
    colors = color_string.split('-')            
    colors.sort()                                 
    return '-'.join(colors)                       

input_colors = "green-red-yellow-black-white"
output = sort_colors(input_colors)
print(output)

'''
2. Create a Python module with the following functions:-
Function name                  task
ispalindrome(name)             given the user name as input,this function should tell us whether the name is palindrome or not.
count_the_vowels(name)         this function should tell us how many vowels are present in it.
frequency_of_letters(name)     this function should tell us how many times each letter appears in the name

'''

def ispalindrome(name):
    name = name.lower()
    if name == name[::-1]:
        return True
    else:
        return False

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    freq = {}
    for char in name:
        char = char.lower()
        if char.isalpha(): 
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

if __name__ == "__main__":
    username = input("Enter a name: ")

    print("\nIs Palindrome:", ispalindrome(username))
    print("Vowel Count:", count_the_vowels(username))

    print("Letter Frequency:")
    freq_result = frequency_of_letters(username)
    for letter, count in freq_result.items():
        print(f"{letter}: {count}")

