#!/usr/bin/python
import math
# ==========================================================================
#!/usr/bin/python

class Account(object):
        _accountName = ""
        _balance = 0.0
        _transactions = 0

        #constructor
        def __init__(self, accountName=None, bal=0.0):
                self._accountName = accountName
                self._balance = bal

        #getter
        def getBalance(self):
                return self._balance

        #deposits money into account
        def deposit(self, amount):
                self._balance += amount
                self._transactions += 1
                return self._balance

        #withdraws money from account, returns False if insufficient funds
        def withdraw(self, amount):
                if amount <= self._balance:
                        self._balance -= amount
                        self._transactions += 1
                        return self._balance
                else:
                        return False

        #overload len(), returns transaction count
        def __len__(self):
                return self._transactions

        #overloads str(), returns account name
        def __str__(self):
                return self._accountName

        #overloads "==", returns True if two account balances match
        def __eq__(self, other):
#               return self._balance == other.getBalance()      #why doesn't this work?
                return self._balance == other._balance

class CreditAccount(Account):
        __limit = 0.0
        __rate = 0.0

        #constructor
        def __init__(self, accountName=None):
                self._accountName = accountName
                self._balance = 0.0
                self.__limit = 1000.00
                self.__rate = 1.24

        #removes debt
        def deposit(self, amount):
                        self._balance -= amount
                        if self._balance < 0:
                                self._balance = 0.0
                        return self._balance

        #withdraws credit at rate
        def withdraw(self, amount):
                if (self._balance + amount) < self.__limit:
                        self._balance += amount * self.__rate
                        self._transactions += 1
                        return self._balance
                else:
                        return False

class SavingsAccount(Account):

        def deposit(self, amount):
                self._balance += amount * 1.05
                self._transactions += 1
                return self._balance

        def accrue(self):
                self._balance = self._balance * 1.05
                return self._balance
# ==========================================================================
## DO NOT MODIFY BEYOND THIS POINT!
## Submissions with modifications beyond this line will be given a 0 score
## We will check... we have the technology :-)
if __name__ == "__main__":
    myScore = 0
    # Test base account
    acct = Account('Chelsey', 1024.32)
    # test withdraw method overdraft
    if acct.withdraw(100000.00) == False:
        myScore += 5
    else:
        print("ERROR: Account.withdraw(ammount) did not return False.")
    # Test withdraw method balance OK
    if acct.withdraw(60.01) == 964.31:
        myScore += 5
    else:
        print("ERROR: Value returned when attempting to make a withdrawal was unexpected")
    # test deposit function
    if acct.deposit(36.50) == 1000.81:
        myScore += 5
    else:
        print("ERROR: The deposit function on Account class returned an unexpected value")
    # test transaction counter
    if len(acct) == 2:
        myScore += 5
    else:
        print("ERROR: The transaction counter returned an unexpected result when using len()")
    # Check toString()
    if str(acct) == 'Chelsey':
        myScore += 5
    else:
        print("ERROR: Converting Account to a string had an unexpected resule")
    # Test equivilance operator
    acct2 = Account('Sam', 1000.81)
    if acct == acct2:
        myScore += 5
    else:
        print("ERROR: Equivilance op test #1 failed")
    acct2.withdraw(1000.00)
    if acct == acct2:
        print("ERROR: Equivilance op test #2 failed")
    else:
        myScore += 5
    # Test the CreditAccount class
    acct = CreditAccount('Chelsey')
    # Test inherited methods
    if str(acct) == 'Chelsey':
        myScore += 5
    else:
        print("ERROR: When testing inherited methods for CreditAccount")
    
    # Test withdraw function
    if acct.withdraw(100000.00) == False:
        myScore += 5
    else:
        print("ERROR: CreditAccount.withdraw did not return expected false")
    if acct.withdraw(100.00) == 124.00:
        myScore += 5
    else:
        print("ERROR: CreditAccount.withdraw returned unexpected result")
    # test deposit function
    if acct.deposit(100.00) == 24.00:
        myScore += 5
    else:
        print("ERROR: CreditAccount.deposit returned unexpected result")
    
    # test transaction counter
    if len(acct) == 1:
        myScore += 5
    else:
        print("ERROR: CreditAccount length was incorrect")
    # test SavingsAccount
    acct1 = SavingsAccount('Hannah', 36.30)
    acct2 = SavingsAccount('Andrew', 156.33)
    if acct1.deposit(100.00) == 141.30:
        myScore += 5
    else:
        print("ERROR: deposit for savings account had unexpected return")
    # test accrue
    if acct1.accrue() == 148.365:
        myScore += 5
    else:
        print("ERROR: deposit for savings account had unexpected return")
    print("Grading complete: your score is %d out of 70" % (myScore) )
