# -------------------------_Practice_----------------------------------------------
# list = [1, 2, 3, 5, 8]
# new = [i + 1 for i in list]
# name = 'hh'
# letter = [i for i in name]
# rangelist = [i * 2 for i in range(0, 10)]
# names = ['a', 'b', 'c']
# short_names = [i for i in names if len(i) < 3]
# l_names = [i.upper() for i in names if len(i) < 3]
# squared = [i * i for i in list]
# even = [i for i in list if i%2 == 0]
#
# print(new)
# print(letter)
# print(rangelist)
# print(short_names)
# print(l_names)
# print(squared)
# print(even)


# Dictionary: new_dic = {new_key:new_value for (key, value) in dic.items() if test}
# import random
# names = ['Ram', 'Hari', 'Sita', 'Rita', 'Beta']
# score = [10, 20, 30, 40, 50]
# student_scores = {i:random.randint(1,100) for i in names}
# passed_students = {student:score for (student, score)  in student_scores.items()  if score > 32}
#
# print(student_scores)
# print(passed_students)

# Looping from dictionary
students = {
    'student': ['Tarun', 'arun', 'kima'],
    'score': [50, 60, 70]
}
for (key, value) in students.items():
    print(key)

import pandas

students_df = pandas.DataFrame(students)
print(students_df)
