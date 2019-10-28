class Student:
  # for every class (built in / user defined) a single object is create in the ram
  # this object holds the class definition
  # class object

  count = 0 # class attribute
  # access class attrbute
  # class name.attribute name

  def __init__(self, name, gender, roll, marks=0, contact_nos=None):
    # None means variable which does not refer to any object. Like null
    # create attributes in the object
    # constructor

    # object attributes
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks
    self.contact_nos = contact_nos

    Student.count += 1

  def get_details(self):
    # self - current object for which the method was intended to be called (Student)
    '''part1 = 'Name : ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + str(self.roll) \
    + '\nMarks: ' + str(self.marks) + '\n' '''
    ''' part1 = 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(\
      self.name, self.gender, self.roll, self.marks) '''
    part1 = 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'.format(gender=self.gender,\
      name=self.name, roll=self.roll, marks=self.marks)

    part2 = 'Contact Nos: '
    if self.contact_nos:
      for contact_no in self.contact_nos:
        part2 += '\n' + contact_no
    else:
      part2 += 'NA'
    
    return part1 + part2

  def get_grade(self):
    marks = self.marks
    if marks > 100 or marks < 0:
      grade = 'I'
    elif marks >= 70:
      grade = 'A'
    elif marks >= 60:
      grade = 'B'
    elif marks >= 40:
      grade = 'C'
    else:
      grade = 'F'
    return grade

  def get_count():
    # class methods do not have self
    # class methods will never have a requirement to access attributes of an object
    return Student.count

  def get_name_roll(self):
    return (self.name, self.roll)