# parent class / super class / base class
class CollegeUser(object): # every class in python implicitly inherits from the class object
  def __init__(self, name, gender, contact_nos=None):
    # self - Student object, Professor object, sub class object of CollegeUser
    self.name = name
    self.gender = gender
    self.contact_nos = contact_nos

  def get_details(self):
    # self will be student object, professor object
    return 'Name: {0}\nGender: {1}'.format(self.name.upper(), self.gender)

  def __str__(self):
    return 'Name: {0}\nGender: {1}'.format(self.name.upper(), self.gender)
