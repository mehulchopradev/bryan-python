from com.abc.lib.student_ops import get_details, get_grade


name = input('Enter name: ')
gender = input('Enter gender: ')
roll = int(input('Enter roll: '))
marks = float(input('Enter marks: '))

print(get_details(name, gender, roll, marks))
print(get_grade(marks))

