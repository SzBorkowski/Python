# word = input("Write down a word: ")
# letters = [x for x in word]
# import random
#
# names = ["Alex", "Stanley", "David"]
#
# students_scores = {student:random.randint(1, 100) for student in names}
#
# print(students_scores)
#
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#
# print(passed_students)

# student_dict = {
    # "student": ["Angela", "James", "Lily"],
    # "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
is_on = True
while is_on:
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Incorrect input.")
        word = input("Enter a word: ").upper()
    else:
        print(output_list)
        is_on = False