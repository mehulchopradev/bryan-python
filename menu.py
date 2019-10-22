'''
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 1
Enter n : 8
0 1 1 2 3 5 8 13
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 2
Enter n : 6
0 2 4 6
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 3
Enter n : 9
Odd
1. Fibo Series
2. Even Series
3. Even or Odd
4. Exit
Enter ur choice: 4
'''

# module name -> menu

# google -> google.com
# com.google -> 

# only imports the modules
# import series

# importing only the functions from the module; but not the module
# from series import get_fibo_series as fibo, get_even_series
from com.abc.lib.series import get_fibo_series as fibo, get_even_series

import com.abc.lib.math as mymath

from math import factorial

while True:
  print('1. Fibo series\n2. Even Series\n3. Even or Odd\n4. Factorial\n5. Exit')
  choice = int(input('Enter choice: '))

  if choice == 5:
    break # breaks out forcibly from the enclosing loop (and not branching statement)
  n = int(input('Enter n: '))
  if choice == 1:
    # fibo series
    # pass # pass this block as an empty block without the python environment flagging this as an syntax error
    print(fibo(n))
  elif choice == 2:
    # even series
    print(get_even_series(n))
  elif choice == 3:
    # even or odd
    # print(com.abc.lib.math.evenodd(n))
    print(mymath.evenodd(n))
  else:
    print(factorial(n))