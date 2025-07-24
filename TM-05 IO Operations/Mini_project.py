''' 
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let’s surprise him by breaking the challenge with our python code.
Hints to find the secret message:
The number of lines in the file tells you the meeting time.
Note: 1 <= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12-hour format.
For example:
If the number of lines is 15, then the meeting time is 3 PM.
If the number of lines is 10, then the meeting time is 10 AM.
The word appearing for the maximum number of times tells you the meeting place.
Note: Meeting place will be a street name.
For example:
If the word Oxford appears for the maximum number of times, then meeting place is Oxford Street.
If the word Park appears for the maximum number of times, then meeting place is Park Street.
Sample input 1:
Cricket, a bat-and-ball park game played between two teams of eleven park players on a field at the park center of which is a 20-metre (22-yard) pitch with a wicket at each end, each park comprising two bails balanced on three stumps.
The batting park scores runs by striking the ball bowled at the park wicket with the park bat, while the bowling and park fielding side tries to prevent this and dismiss each park player (so they are "out").
Means of park include being bowled, when the ball hits the park and dislodges the bails, and by the fielding side park the ball after it is hit by the bat, but before it hits the park.
When ten park have been dismissed, the innings ends and the teams park roles.
Sample Output 1:
Meeting time: 9 AM
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of 15 times.
 '''

filename = input("Enter the filename: ")
f = open(filename, "r")
lines = f.readlines()
f.close()

# Step 1: Calculate meeting time from line count
n_lines = len(lines)
if n_lines > 12:
    meeting_time = f"{n_lines % 12} PM"
else:
    meeting_time = f"{n_lines} AM"

# Step 2: Count word frequencies
word_count = {}
for line in lines:
    words = line.strip().lower().replace('.', '').replace(',', '').split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

# Step 3: Find the most frequent word
most_freq_word = max(word_count, key=word_count.get)
meeting_place = most_freq_word.capitalize() + " Street"

# Output
print("Meeting time:", meeting_time)
print("Meeting place:", meeting_place)
