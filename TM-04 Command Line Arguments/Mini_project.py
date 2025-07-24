'''
Task Description:-
Through command line arguments three strings separated by space are given to y.Each string is a series of numbers separated by hyphen.
You like all the numbers in string 1 and dislike all the numbers in string 2.
Third string contains the numbers given to you.Your initial happiness is 0. 
When you encounter a number present in string 1,add 1 to your happiness ,
if it is present in string 2,add -1 to your happiness.Otherwise ,yoour happiness does not change.
Output your final happiness at the end.

Sample input 1:3-15-71-5-3-8
Sample output 1:1

Explanation:
Numbers in string 1:3, 1
Numbers in string 2:5, 7
Numbers given to you:1, 5, 3, 8

You gain 1 unit of happiness for numbers 1 and 3 which are in string 1.
Your total happiness is 2 now.

You lose 1 unit of happiness for number 5 which is in string 2.
Your total happiness is 1 now.

8 is not present in either of the strings, so your happiness does not change.

Final happiness is 1.

'''

import sys

# Check if three arguments are passed (excluding script name)
if len(sys.argv) != 4:
    print("Please provide exactly three hyphen-separated strings.")
    sys.exit(1)

# Read strings from command line arguments
liked_str = sys.argv[1]
disliked_str = sys.argv[2]
given_str = sys.argv[3]

# Convert hyphen-separated strings to sets of integers
liked_numbers = set(map(int, liked_str.split('-')))
disliked_numbers = set(map(int, disliked_str.split('-')))
given_numbers = list(map(int, given_str.split('-')))

# Initialize happiness
happiness = 0

# Compute happiness
for num in given_numbers:
    if num in liked_numbers:
        happiness += 1
    elif num in disliked_numbers:
        happiness -= 1

# Output final happiness
print(happiness)
