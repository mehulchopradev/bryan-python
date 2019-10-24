from com.abc.lib.math import evenodd

pointers = [6, 7, 6, 10, 1, 2, 3, 7, 8, 4, 9]

# get a new list of even pointers from pointers list (Filtering)
'''evens = []
for pointer in pointers:
  if evenodd(pointer) == 'Even':
    evens.append(pointer)'''

# for comprehensions
# u shud be needing a new list
evens = [pointer for pointer in pointers if evenodd(pointer) == 'Even']
print(evens)

# get a new list of odd poinnters greater than 5 (Filtering)
odds = [pointer for pointer in pointers if evenodd(pointer) == 'Odd' and pointer > 5]
print(odds)

# get a new list of deducted by 1 poointer marks (Mapping)
deducted_marks = [pointer - 1 for pointer in pointers]
print(deducted_marks)

# get a new list of deducted by 1 pointer marks of all the even pointers in pointers list (Filtering + Mapping)
dm = [pointer - 1 for pointer in pointers if evenodd(pointer) == 'Even']
print(dm)