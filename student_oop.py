from com.abc.college.student import Student
# print(Student.count)
print(Student.get_count())

# class methods. They are called on the class
# Internally
# Student.getCount()

s1 = Student('mehul', 'm', 10, 67) # 4003 - Student
s1.name = 'Mehul'
# Internally
# 1. 4003 -> memory is reserved for Student object
# 2. Student.__init__(4003, 'mehul', 'm', 10, 67)

# create an attriute in an object
'''s1.name = 'mehul chopra'
s1.gender = 'm'
s1.roll = 10
s1.marks = 67'''


s2 = Student('bryan', 'm', 11, 92) # 4009 - Student
# Internally
# 1. 4009 -> memory is reserved for Student object
# 2. Student.__init__(4009)

print(Student.count)

'''s2.name = 'bryan'
s2.gender = 'm'
s2.roll = 11
s2.marks = 92'''

name = 'mehul chopra' # 5004 - str

s3 = Student(name='jane', gender='f', roll=11) # 4008 - Student
'''s3.student_name = 'jane'
s3.gen = 'f'
s3.r = 11
s3.marks = 80'''

# access the attributes from an object
'''print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll)'''

print(Student.count)
print(s1.get_details())
# Internally
# Student.get_details(s1)


print(s2.get_details())
# Internally
# Student.get_details(s2)

print(s3.get_details())

print(s1.get_grade())
# Student.get_grade(s1)

print(s2.get_grade())
# Student.get_grade(s2)