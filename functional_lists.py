pointers = [10, 10, 5, 6, 3, 4, 8, 10, 1]

# higher order function - That does all the looping on the list and collecting of data in new list for us (static)
# lower order function -  Logic that should execute in the above loop (dynamic)

'''def filter(elements, fn):
  result = []
  for element in elements:
    if fn(element):
      result.append(element)

  return result'''


# get a new list of all the even elements from pointers list
'''def even_elements(ele): # lower order functions
  return not ele % 2

# evens = filter(pointers, even_elements)
evens = filter(even_elements, pointers)
print(list(evens))'''

# lambda functions (annonymous functions)
evens = filter(lambda ele: not ele % 2, pointers)
print(list(evens))

# get a new list of odd elements greater than or equal to 3 from pointers list
'''def odds_greater_equal_3(ele): # lower order functions
  return ele % 2 and ele >= 3
# odds = filter(pointers, odds_greater_equal_3)
odds = filter(odds_greater_equal_3, pointers)
print(list(odds))'''

odds = filter(lambda ele: ele % 2 and ele >= 3, pointers)
print(list(odds))

# get a new list of sqaures of even elemennts and cubes of odd element from pointers list (Mapping)
def even_odd(ele):
  return ele ** 2 if not ele % 2 else ele ** 3

evenodds = map(even_odd, pointers)
print(list(evenodds))


def for_each(fn, elements):
  for element in elements:
    fn(element)

# print only even elements greater than 4 from the pointers list (for -  each)
def print_even(ele):
  if not ele % 2 and ele > 4:
    print(ele)
for_each(print_even, pointers)

print('Squares of odds more than 3')
# print only squares of odds greater than or equal 3
def odds_more_than_3(ele):
  if ele % 2 and ele > 3:
    print(ele)
for_each(odds_more_than_3, pointers)