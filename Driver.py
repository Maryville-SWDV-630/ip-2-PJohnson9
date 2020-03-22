# Patrick Johnson         3/22/2020 #
# SWDV 630 3W 20/SP2         Week 2 #
#####################################
# Driver application for Checking Account class

from CheckingAccount import *

johnAddress = Address("123 Main Street", "Anytown", "MO", "63100")

account = CheckingAccount(78946123, "John Smith", johnAddress, 0)

account.creditAccount(500) # $500 Deposit
print(account.getBalance())

account.debitAccount(50)   # $50 Withdrawal
print(account.getBalance())

account.creditAccount(500) # $500 Deposit
print(account.getBalance())

account.debitAccount(1000) # $1000 Withdrawal
print(account.getBalance())