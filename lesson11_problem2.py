print('-' * 60)
print('Narrative Bot:')
print()
name = input('what is the name of student? ')
grade = input('What is the grade? ')
grade = int(grade)
if grade < 65:
	print(name + 'your final grade in AP computer science is' + grade + 'and you are doing great keep on the good work.') 
else:
	print(name + 'your final grade in AP computer science is' + grade + 'and you are doing bad, please come for tutoring.')
	print('-' * 60)