#1. WAP to find check if a string has only octal digits.Given string ['789','123','004']
import re
data = ['789', '123', '004']
for s in data:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s} is an octal number")
    else:
        print(f"{s} is NOT an octal number")

#2. Extract the user id,domain name and suffix from the following email id.
import re
email = "user.name@example.co.in"
match = re.match(r'([\w\.]+)@([\w]+)\.([\w\.]+)', email)
if match:
    user_id = match.group(1)
    domain = match.group(2)
    suffix = match.group(3)
    print("User ID:", user_id)
    print("Domain:", domain)
    print("Suffix:", suffix)

#3. Split the following irregular sentence into proper words
# sentence = """A, very very; irregular_sentence"""
# expected output : A very very irregular sentence 
import re
sentence = """A, very    very; irregular_sentence"""
cleaned = re.sub(r'[^\w\s]', '', sentence)        
cleaned = re.sub(r'[_\s]+', ' ', cleaned).strip() 
print(cleaned) 

#4. Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
#tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
#desired_output = ' Good advice What I would do differently if I was learning to code today'
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
cleaned = re.sub(r"http\S+|@\S+|#\S+|RT|cc:?", "", tweet)  
cleaned = re.sub(r'[^\w\s]', '', cleaned)               
cleaned = re.sub(r'\s+', ' ', cleaned).strip()            
print(cleaned)

#5. Extract all the text portions between the tags from the following HTML page:
import re
import requests
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
html = requests.get(url).text
matches = re.findall(r'>([^<>]+)<', html)
cleaned = [text.strip() for text in matches if text.strip()]
print(cleaned)

#6. Given below list of words, identify the words that begin and end with the same character.
import re
words = ['civic', 'trust', 'widows', 'maximum']
matching = [word for word in words if re.fullmatch(r'(.).*\1', word)]
print(matching) 
