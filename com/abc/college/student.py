from .college_user import CollegeUser
# child class / sub class / concrete class

class Student(CollegeUser):
  def __init__(self, name, gender, roll, marks, contact_nos=None):
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks

  # method overriding
  # overriden method will always be called over the super class inherited method
  def get_details(self):
    part1 = super().get_details()
    return '{0}\nRoll: {1}'.format(part1, self.roll)

  # can have their own set of methods too