from com.abc.college.student import Student

'''slist = [
  Student('mehul', 'm', 10),
  Student('bryan', 'm', 5),
  Student('jane', 'f', 23)
]'''

smap = {
  10: Student('mehul', 'm', 10),
  5: Student('bryan', 'm', 5),
  23: Student('jane', 'f', 23)
}

roll = int(input('Enter roll to search : '))

'''for student in slist:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  # will execute when the corresponding for block is completely exhausted
  # when in the corresponding for block there is no break encountered
  print('Student not found')'''

if roll in smap:
  student = smap[roll]
  print(student.get_details())
else:
  print('Student not found')