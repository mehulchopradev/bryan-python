from com.abc.college.student import Student
from com.abc.college.professor import Professor
s1 = Student('mehul', 'm', 10, 90, ['98798789'])
# Student.__init__(4003, 'mehul', 'm', 10, 90, ['98798789'])

p1 = Professor('jane', 'f', ['Physics'], ['345345345'])
# Professor.__init__(4005, 'jane', 'f', ['Physics'], ['345345345'])

'''print(s1.name)
print(s1.gender)

print(p1.name)
print(p1.gender)'''

# print(s1.get_details())
# Student.get_details(3003)

# print(p1.get_details())
# Professor.get_details(3004)

name = 'mehul chopra'

print(name)
# internally
# print(name.__str__())
# print(str.__str__(name))

print(s1)
# internally
# print(s1.__str__())
# print(Student.__str__(s1))