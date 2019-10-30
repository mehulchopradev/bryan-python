from com.abc.bank.account import Account
from traceback import print_exc

a = Account(1234, 'mehul', 10000)


'''try:
  ub = a.withdraw(-5000)
except PermissionError:
  print_exc()
except ValueError:
  print_exc()
except Exception:
  print('From here')
  print_exc()
else:
  print(ub)'''

try:
  ub = a.withdraw(9500)
except Exception:
  # a catch all exception block
  print('From here')
  print_exc()
else:
  print(ub)