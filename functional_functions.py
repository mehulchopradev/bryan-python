def abc():
  i = 3 # int -> i: abc
  j = 5 # int -> j: abc
  k = 9 # int -> k: abc
  m = 10 # int -> m: abc

  # in python a function can be defined inside another function
  def pqr(): # function -> pqr: abc
    print(i) # can access the outer function variables
    j = 10 # int -> j: pqr
    print(j) # 10

    # k += 10 # will not work. Reference before assignment
    # print(k)

    global m
    m = 30 # m to refer to the enclosing function variable
    print(m)
    # m += 20 # m to refer to the enclosing function variable

  print(m)
  pqr()
  print(m)
  print(j) # 5
  print(k) # 9

abc()
# pqr() # will not work


def mno(k):
  def rty(i):
    j = i + 10 + k
    return j

  # a function can return another function in python
  return rty

m = mno(20) # m - rty - callable
print(m(5))

# function -> kkr: module
def kkr(f):
  i = 10
  j = f(i) # func(el)
  return j ** 2

# function -> func: module
def func(el):
  return el + 10

print(kkr(func))
# pass a function as an argument to another function
# callback functions