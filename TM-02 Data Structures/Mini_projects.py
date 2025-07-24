#1. Create a dictionary that contains a list of people and one interesting fact about each of them. Display each person and their interesting fact. 
# Change a fact about one of the people, add an additional person, and display the updated list. Run the program multiple times to observe if the order changes.
facts = {
    'Jeff': 'Is afraid of Dogs.',
    'David': 'Plays the piano.',
    'Jason': 'Can fly an airplane.'
}

for person, fact in facts.items():
    print(f"{person}: {fact}")

print()  

facts['Jeff'] = 'Is afraid of heights.'

facts['Jill'] = 'Can hula dance.'
for person, fact in facts.items():
    print(f"{person}: {fact}")

#2. Given a list of participant scores for your University Sports Day, determine the score of the runner-up (the second highest unique score)

scores = [2, 3, 6, 6, 5]

unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

runner_up = unique_scores[1]

print(runner_up)

#3. You have a record of n students.Each record contains the student's name ,and their percent marks in Maths,Chemistry,Physics.The marks can be floating value.
# You are required to save the record in a dictionary data type.Student's key is the key.Marks stored in the list is the value.The user enters a student's name.
#Output the average percentage marks obtained by that student.
def average_percentage_marks(records, student_name):
    if student_name in records:
        marks = records[student_name]
        average = sum(marks) / len(marks)
        return average
    else:
        return None

#4. Given a sring of n words,help Alex to find out how many times his name appears in the string.    

input_string = "Hi Alex WelcomeAlex Bye Alex."

name_to_count = "Alex"


count = input_string.count(name_to_count)

print(count)