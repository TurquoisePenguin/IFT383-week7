#!/usr/bin/python

class Account(object):
#	_accountName = ""
#	_balance = 0.0
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
#		return self._balance == other.getBalance()	#why doesn't this work?
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
