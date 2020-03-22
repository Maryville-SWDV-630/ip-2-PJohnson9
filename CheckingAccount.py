# Patrick Johnson         3/22/2020 #
# SWDV 630 3W 20/SP2         Week 2 #
#####################################
# Checking Account class

from datetime import datetime

class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip


class CheckingAccount:
    def __init__(self, accountNumber, name, address, balance = 0, openingDate = datetime.now()):
        self.accountNumber = accountNumber
        self.openingDate = openingDate
        self.name = name
        self.address = address
        self._balance = balance
        
    def getBalance(self):
        return self._balance
    
    def creditAccount(self, creditAmount):
        self._balance += creditAmount
        
    def debitAccount(self, debitAmount):
        self._balance -= debitAmount
