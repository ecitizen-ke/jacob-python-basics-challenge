'''
Nested Lists:
- Create a nested list containing three inner lists, each representing a student's scores in three
subjects.
- Calculate the average score for each student and store it in a separate list.
- Print out the average score for each student.
'''
student_scores = [
[30,60,50],
[90,76,49],
[80,70,35]
        ]
average_scores=[]

for student_score in student_scores:
    average=sum(student_score)/len(student_score)
    average_scores.append(average)


print(average_scores)
for average in average_scores:
    print(average)


