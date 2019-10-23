class Student:
  # for every class (built in / user defined) a single object is create in the ram
  # this object holds the class definition
  # class object

  count = 0 # class attribute
  # access class attrbute
  # class name.attribute name

  def __init__(self, name, gender, roll, marks=0):
    # create attributes in the object
    # constructor

    # object attributes
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    Student.count += 1

  def get_details(self):
    # self - current object for which the method was intended to be called (Student)
    return 'Name : ' + self.name + '\nGender: ' + self.gender + '\nRoll: ' + str(self.roll) \
    + '\nMarks: ' + str(self.marks)

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