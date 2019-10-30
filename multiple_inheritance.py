# vendor 1
class A:
  def fun(self):
    print('Fun of A')

  def show(self):
    print('Show of A')

# vendor 2
class B:
  def show(self):
    print('Show of B')

class C(B, A): # one sub class having more than 1 direct super class
  # MRO (Method resolution order)
  pass

c = C()
c.fun()
c.show()