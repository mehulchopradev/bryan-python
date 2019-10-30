'''print('Program starts')

n = input('Enter n: ')

ni = int(n)
print('Odd') if ni % 2 else print('Even')

print('Program ends')'''

'''
Right input
Python environment -> play_input -> n='5' -> int() -> ni=5 -> Odd -> Program ends

Wrong input
Python environment -> play_input -> n='good' -> int() -> raises (throws) ValueError object -> line 5 ->
raises (throws) ValueError object -> Python environment

Changed flow
Python environment -> play_input -> n='good' -> int() -> raises (throws) ValueError object -> int(n)
-> play_input should only handle the error -> Program ends
'''

from traceback import print_exc

print('Program starts')

n = input('Enter n: ')

# handle the error over here itself
try:
  ni = int(n)
except ValueError:
  # print('Please enter integer value')
  print_exc() # prints the error stack trace (traceback)
else:
  # will execute when there is no exception (error) in the corresponding try block
  print('Odd') if ni % 2 else print('Even')

print('Program ends')