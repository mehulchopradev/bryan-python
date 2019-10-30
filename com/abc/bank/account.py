class Account:
  min_balance = 1000

  def __init__(self, acc_no, acc_name, acc_balance):
    self.acc_no = acc_no
    self.acc_name = acc_name
    self.acc_balance = acc_balance

  def withdraw(self, amt):
    if amt <= 0:
      raise ValueError('Amt to withdraw must be positive and non zero')
    if self.acc_balance - amt < Account.min_balance:
      # raise an error to the caller of withdraw()
      raise PermissionError('Cannot withdraw now as balance is low')

    self.acc_balance -= amt
    return self.acc_balance