#1. WAP to read the entire content from the text file and display it to the user.
filename = input("Enter file name: ")
file = open(filename, 'r')
content = file.read()
file.close()
print("File Contents:\n", content)

#2. WAP to read first n lines from the text file .Get n as user input.
filename = input("Enter file name: ")
n = int(input("Enter number of lines to read: "))
file = open(filename, 'r')
for i in range(n):
    line = file.readline()
    if not line:
        break
    print(line.strip())
file.close()

#3. WAP to accept input from user and append it to a text file.
filename = input("Enter file name: ")
data = input("Enter text to append: ")
file = open(filename, 'a')
file.write(data + '\n')
file.close()
print("Text appended successfully.")


#4. WAP to read contents from a text file line by line and store each line into a list.
filename = input("Enter file name: ")
file = open(filename, 'r')
lines = [line.strip() for line in file]
file.close()
print("Lines as list:", lines)

#5. WAP to find the longest word from the text file contents,assuming that the file will have only one longest word in it.
filename = input("Enter file name: ")
file = open(filename, 'r')
words = file.read().split()
file.close()
longest = max(words, key=len)
print("Longest word in the file is:", longest)


#6. WAP to count the frequency of a user entered word in a text file.
filename = input("Enter file name: ")
search_word = input("Enter word to search: ")
file = open(filename, 'r')
content = file.read().lower().split()
file.close()
count = content.count(search_word.lower())
print(f"The word '{search_word}' appears {count} times in the file.")

