n = int(input('Enter n: '))

# if - else
'''
if expression - truthy / falsy:
  I1
  I2
else:
  I1
  I2
'''

'''if n % 2:
  print('Odd')
else:
  print('Even')'''

# if comprehensions
# Both the branches must have only a single instruction execute
print('Odd') if n % 2 else print('Even')
