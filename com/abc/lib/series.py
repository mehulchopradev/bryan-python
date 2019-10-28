# house all library functions related to series generation
# every python file is by default a module
# name of the module -> name of the file without the py
# series

def get_fibo_series(n):
  result = ''
  a, b = 0, 1
  result = result + str(a) + '\t' + str(b) + '\t' # in python only str data can be concatenated with str data

  for v in range(3, n + 1):
    c = a + b
    result = result + str(c) + '\t'
    a, b = b, c
  print(v) # last value in the for loop
  print(c) # last value in the for loop
  # scope of variables in python is never the block scoped (which is true in languages like java)
  # scope is rather the enclosing function (if it exists) or the entire module
  return result

def get_even_series(n):
  result = ''

  for v in range(0, n + 1, 2):
    result += str(v) + '\t'
  return result